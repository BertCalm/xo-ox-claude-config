#!/usr/bin/env python3
"""Python 3.9-compatible trigger test for skill descriptions.
Tests whether a skill description causes Claude to invoke the skill for given queries."""

import json
import os
import select
import subprocess
import sys
import time
import uuid
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import Dict, List, Optional


def find_project_root():
    current = Path.cwd()
    for parent in [current, *current.parents]:
        if (parent / ".claude").is_dir():
            return parent
    return current


def parse_skill_md(skill_path):
    skill_file = Path(skill_path) / "SKILL.md"
    content = skill_file.read_text()
    name = ""
    description = ""
    in_frontmatter = False
    body_lines = []
    frontmatter_done = False
    for line in content.split("\n"):
        if line.strip() == "---" and not frontmatter_done:
            if not in_frontmatter:
                in_frontmatter = True
                continue
            else:
                in_frontmatter = False
                frontmatter_done = True
                continue
        if in_frontmatter:
            if line.startswith("name:"):
                name = line.split(":", 1)[1].strip().strip('"')
            elif line.startswith("description:"):
                description = line.split(":", 1)[1].strip().strip('"')
        elif frontmatter_done:
            body_lines.append(line)
    return name, description, "\n".join(body_lines)


def run_single_query(query, skill_name, skill_description, timeout, project_root, model=None):
    unique_id = uuid.uuid4().hex[:8]
    clean_name = "{}-skill-{}".format(skill_name, unique_id)
    project_commands_dir = Path(project_root) / ".claude" / "commands"
    command_file = project_commands_dir / "{}.md".format(clean_name)

    try:
        project_commands_dir.mkdir(parents=True, exist_ok=True)
        indented_desc = "\n  ".join(skill_description.split("\n"))
        command_content = (
            "---\n"
            "description: |\n"
            "  {}\n"
            "---\n\n"
            "# {}\n\n"
            "This skill handles: {}\n"
        ).format(indented_desc, skill_name, skill_description)
        command_file.write_text(command_content)

        cmd = [
            "claude",
            "-p", query,
            "--output-format", "stream-json",
            "--verbose",
            "--include-partial-messages",
        ]
        if model:
            cmd.extend(["--model", model])

        env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}

        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            cwd=project_root,
            env=env,
        )

        start_time = time.time()
        buffer = ""
        pending_tool_name = None
        accumulated_json = ""

        try:
            while time.time() - start_time < timeout:
                if process.poll() is not None:
                    remaining = process.stdout.read()
                    if remaining:
                        buffer += remaining.decode("utf-8", errors="replace")
                    break

                ready, _, _ = select.select([process.stdout], [], [], 1.0)
                if not ready:
                    continue

                chunk = os.read(process.stdout.fileno(), 8192)
                if not chunk:
                    break
                buffer += chunk.decode("utf-8", errors="replace")

                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    line = line.strip()
                    if not line:
                        continue

                    try:
                        event = json.loads(line)
                    except json.JSONDecodeError:
                        continue

                    if event.get("type") == "stream_event":
                        se = event.get("event", {})
                        se_type = se.get("type", "")

                        if se_type == "content_block_start":
                            cb = se.get("content_block", {})
                            if cb.get("type") == "tool_use":
                                tool_name = cb.get("name", "")
                                if tool_name in ("Skill", "Read"):
                                    pending_tool_name = tool_name
                                    accumulated_json = ""
                                else:
                                    return False

                        elif se_type == "content_block_delta" and pending_tool_name:
                            delta = se.get("delta", {})
                            if delta.get("type") == "input_json_delta":
                                accumulated_json += delta.get("partial_json", "")
                                if clean_name in accumulated_json:
                                    return True

                        elif se_type in ("content_block_stop", "message_stop"):
                            if pending_tool_name:
                                return clean_name in accumulated_json
                            if se_type == "message_stop":
                                return False

                    elif event.get("type") == "assistant":
                        message = event.get("message", {})
                        for content_item in message.get("content", []):
                            if content_item.get("type") != "tool_use":
                                continue
                            tool_name = content_item.get("name", "")
                            tool_input = content_item.get("input", {})
                            if tool_name == "Skill" and clean_name in tool_input.get("skill", ""):
                                return True
                            elif tool_name == "Read" and clean_name in tool_input.get("file_path", ""):
                                return True
                            return False

                    elif event.get("type") == "result":
                        return False
        finally:
            if process.poll() is None:
                process.kill()
                process.wait()

        return False
    finally:
        if command_file.exists():
            command_file.unlink()


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--eval-set", required=True)
    parser.add_argument("--skill-path", required=True)
    parser.add_argument("--model", default=None)
    parser.add_argument("--num-workers", type=int, default=5)
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--runs-per-query", type=int, default=1)
    args = parser.parse_args()

    eval_set = json.loads(Path(args.eval_set).read_text())
    name, description, _ = parse_skill_md(args.skill_path)
    project_root = find_project_root()

    print("Testing description for skill: {}".format(name), file=sys.stderr)
    print("Queries: {}".format(len(eval_set)), file=sys.stderr)
    print("Runs per query: {}".format(args.runs_per_query), file=sys.stderr)
    print("", file=sys.stderr)

    with ProcessPoolExecutor(max_workers=args.num_workers) as executor:
        future_to_info = {}
        for item in eval_set:
            for run_idx in range(args.runs_per_query):
                future = executor.submit(
                    run_single_query,
                    item["query"],
                    name,
                    description,
                    args.timeout,
                    str(project_root),
                    args.model,
                )
                future_to_info[future] = (item, run_idx)

        query_triggers = {}  # type: Dict[str, List[bool]]
        query_items = {}  # type: Dict[str, dict]
        for future in as_completed(future_to_info):
            item, _ = future_to_info[future]
            query = item["query"]
            query_items[query] = item
            if query not in query_triggers:
                query_triggers[query] = []
            try:
                query_triggers[query].append(future.result())
            except Exception as e:
                print("Warning: query failed: {}".format(e), file=sys.stderr)
                query_triggers[query].append(False)

    results = []
    for query, triggers in query_triggers.items():
        item = query_items[query]
        trigger_rate = sum(triggers) / len(triggers)
        should_trigger = item["should_trigger"]
        did_pass = (trigger_rate >= 0.5) if should_trigger else (trigger_rate < 0.5)
        results.append({
            "query": query,
            "should_trigger": should_trigger,
            "trigger_rate": trigger_rate,
            "triggers": sum(triggers),
            "runs": len(triggers),
            "pass": did_pass,
        })

    passed = sum(1 for r in results if r["pass"])
    total = len(results)

    print("\n=== RESULTS: {}/{} passed ===\n".format(passed, total), file=sys.stderr)
    for r in sorted(results, key=lambda x: (x["pass"], x["should_trigger"])):
        status = "PASS" if r["pass"] else "FAIL"
        expected = "should_trigger" if r["should_trigger"] else "should_NOT_trigger"
        rate = "{}/{}".format(r["triggers"], r["runs"])
        print("  [{}] rate={} ({}) {}".format(status, rate, expected, r["query"][:80]), file=sys.stderr)

    output = {
        "skill_name": name,
        "description": description,
        "results": results,
        "summary": {"total": total, "passed": passed, "failed": total - passed},
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
