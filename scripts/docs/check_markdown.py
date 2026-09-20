#!/usr/bin/env python3
"""Check Aura-authored Markdown style and references."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BANNED = (
    "just", "simply", "easy", "obviously", "clearly", "basically",
    "utilize", "in order to", "prior to",
)
SKIP = {".git", ".scratch", "node_modules", "vendor", "charts/deepgram-self-hosted"}


def markdown_files() -> list[Path]:
    out = subprocess.check_output(
        ["git", "ls-files", "*.md", "*.MD"],
        cwd=ROOT,
        text=True,
    )
    return [
        Path(line) for line in out.splitlines()
        if not any(part in SKIP for part in Path(line).parts)
        and not Path(line).as_posix().startswith("backend/charts/deepgram-self-hosted/")
    ]


def check(path: Path) -> list[str]:
    text = (ROOT / path).read_text(encoding="utf-8")
    errors: list[str] = []
    lines = text.splitlines()

    if path.name.lower() == "skill.md" and not text.startswith("---\n"):
        errors.append("missing frontmatter")

    depths = [len(m.group(1)) for m in re.finditer(r"^(#+)\s+", text, re.M)]
    if depths and max(depths) > 3:
        errors.append("heading depth > 3")

    lower = text.lower()
    for term in BANNED:
        if re.search(r"\b" + re.escape(term) + r"\b", lower):
            errors.append(f"banned term: {term}")

    for line_no, line in enumerate(lines, 1):
        if re.match(r"^\s*(?:[-*]\s+)?(?:This|It)\b", line):
            errors.append(f"bare sentence opener at line {line_no}")

    prose = re.sub(r"\x60\x60\x60.*?\x60\x60\x60", "", text, flags=re.S)
    for sentence_no, sentence in enumerate(
        re.split(r"(?<=[.!?])\\s+|\\n+", prose),
        1,
    ):
        words = re.findall(r"\\b[\\w’'-]+\\b", sentence)
        if len(words) > 25:
            errors.append(
                f"sentence > 25 words near sentence {sentence_no} ({len(words)} words)"
            )

    return errors


def main() -> int:
    files = markdown_files()
    failures = [
        f"{path}: {error}"
        for path in files
        for error in check(path)
    ]

    for failure in failures:
        print(f"FAIL: {failure}")

    print(f"Checked {len(files)} Markdown files.")
    print(f"{len(failures)} failure(s).")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
