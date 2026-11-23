#!/usr/bin/env python3
"""The One-Line Laugh entry, variant 3.

Writes a single original one-line joke to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). Pure stdlib, deterministic,
no network at runtime.

The joke's mechanism is a scale collision: a tiny pet takes on
the most grown-up financial commitment (a mortgage), and the
punchline lands the consequence on the pet's whole world, the
bowl itself, now in foreclosure. Setup and punchline arrive in
one breath, no setup clause and no second beat, so every word
earns its place.
"""

import os
from pathlib import Path

LINE = "The goldfish took out a mortgage, so our bowl is already in foreclosure."


def validate_line(text: str) -> str:
    """Check the entry against the gate: 1-200 chars, one sentence.

    A single sentence means exactly one terminal full stop, at the
    end, with no other sentence-ending punctuation (no second full
    stop, no question mark, no exclamation mark) anywhere inside,
    and no leading or trailing whitespace.
    """
    text = text.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    if not text or text != text.strip():
        raise SystemExit("entry must not be blank or padded with whitespace")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be a single sentence ending in one full stop")
    if "?" in text or "!" in text:
        raise SystemExit("entry must be a single sentence, no extra sentence endings")
    return text


def main() -> None:
    text = validate_line(LINE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
