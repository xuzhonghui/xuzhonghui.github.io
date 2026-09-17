"""Protect Liquid-looking syntax inside fenced Markdown code blocks.

This script is run only by the Pages build workflow.  It edits the workflow
checkout, not the repository content, so authors can write code examples as-is.
"""

from __future__ import annotations

import re
from pathlib import Path


FENCE_OPEN = re.compile(r"^ {0,3}(`{3,}|~{3,})[^\r\n]*$")


def is_closing_fence(line: str, marker: str) -> bool:
    return bool(re.match(rf"^ {{0,3}}{re.escape(marker[0])}{{{len(marker)},}}[ \t]*$", line))


def protect_code_blocks(path: Path) -> bool:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    result: list[str] = []
    block: list[str] = []
    marker: str | None = None
    changed = False

    for line in lines:
        content = line.rstrip("\r\n")
        if marker is None:
            match = FENCE_OPEN.match(content)
            if match:
                marker = match.group(1)
                block = [line]
            else:
                result.append(line)
            continue

        block.append(line)
        if not is_closing_fence(content, marker):
            continue

        body = "".join(block[1:-1])
        if "{{" in body or "{%" in body:
            newline = "\r\n" if "\r\n" in block[0] else "\n"
            result.extend([block[0], f"{{% raw %}}{newline}", *block[1:-1], f"{{% endraw %}}{newline}", block[-1]])
            changed = True
        else:
            result.extend(block)
        block = []
        marker = None

    if marker is not None:
        result.extend(block)

    if changed:
        path.write_text("".join(result), encoding="utf-8")
    return changed


def main() -> None:
    changed_paths = [path for path in Path("_posts").rglob("*.md") if protect_code_blocks(path)]
    print(f"Protected Liquid syntax in {len(changed_paths)} post(s).")


if __name__ == "__main__":
    main()
