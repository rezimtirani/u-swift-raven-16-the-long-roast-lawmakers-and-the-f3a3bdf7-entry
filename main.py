#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt: a lawmaker who
writes the rules for artificial intelligence, undercut by the one
file format he cannot produce himself.

Standard library only. Writes only to $MAKEFUN_OUTPUT_DIR (or
./output when run locally); never writes into the repository folder.
"""

import os

ROAST = (
    "Congress just passed a bill to govern artificial intelligence, "
    "drafted by a man who prints his emails, signs them, and scans "
    "them back in as a PDF he still cannot open."
)

MAX_CHARS = 320


def validate(text: str) -> str:
    """Enforce the sealed gate: one sentence, 1-320 chars, not blank."""
    cleaned = " ".join(text.split())
    if not cleaned:
        raise SystemExit("roast is blank")
    if len(cleaned) > MAX_CHARS:
        raise SystemExit(f"roast is {len(cleaned)} chars, over 320")
    if cleaned.count(".") > 1:
        raise SystemExit("roast must be a single sentence")
    return cleaned


def main() -> int:
    text = validate(ROAST)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "./output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
