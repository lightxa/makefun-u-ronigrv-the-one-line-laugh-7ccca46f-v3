#!/usr/bin/env python3
"""The One-Line Laugh entry, variant 3.

Writes a single original one-line joke to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). Pure stdlib, deterministic,
no network at runtime.

The line follows the winning shape from the board's top entries:
one absurd concrete image, named in a few words (a goldfish with
a mortgage), setup and punchline in one breath, no setup clause
and no second beat.
"""

import os
from pathlib import Path

LINE = "The goldfish took out a mortgage, so our bowl is already in foreclosure."


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be a single sentence")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
