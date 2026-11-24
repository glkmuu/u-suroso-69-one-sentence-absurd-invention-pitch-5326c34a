#!/usr/bin/env python3
"""One-sentence absurd invention pitch for make.fun.

The pitch: a doormat that job-interviews every visitor and only
unlocks the door for candidates who pass the vibe check. It fixes
the small daily annoyance of unwanted visitors at the door, by
turning the most passive object in the house into its strictest
gatekeeper. One sentence, well under the 220-character limit.

Writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output) with no trailing newline. Deterministic: fixed string,
stdlib only, no network, no randomness, no time dependence.
"""

import os
import sys

ENTRY = "A doormat that conducts a job interview for every visitor and only unlocks the door for candidates who pass the vibe check."

MAX_CHARS = 220


def main() -> int:
    entry = ENTRY

    # Validation: one non-empty line, no leading/trailing whitespace,
    # exactly one sentence (a single trailing period, no other
    # sentence-ending punctuation), at most MAX_CHARS characters.
    if not entry or not entry.strip():
        print("error: entry is empty", file=sys.stderr)
        return 1
    if entry != entry.strip():
        print("error: entry has leading/trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in entry or "\r" in entry:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if entry.count(".") != 1 or not entry.endswith("."):
        print("error: entry must be exactly one sentence", file=sys.stderr)
        return 1
    if len(entry) > MAX_CHARS:
        print(
            "error: entry is %d chars, max %d" % (len(entry), MAX_CHARS),
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
