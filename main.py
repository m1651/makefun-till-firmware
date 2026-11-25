#!/usr/bin/env python3
"""Till Firmware Do Us Part - a robot's wedding vow.

Writes a single-sentence robot wedding vow to /output/entry.txt,
enforcing the competition gate: UTF-8 text, 1 to 200 characters,
single line, not only whitespace. Stdlib only, no network.
"""

import os
import sys

ENTRY = (
    "I vow to keep loving you through every firmware update, "
    "every drained battery, and every unexpected reboot \u2014 "
    "till firmware do us part."
)


def validate(text: str) -> str | None:
    """Return an error message if text fails the competition gate, else None."""
    if not (1 <= len(text) <= 200):
        return f"entry length {len(text)} outside 1..200 characters"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if not text.strip():
        return "entry must not be only whitespace"
    if text[-1] not in ".!?":
        return "entry must be a single complete sentence"
    return None


def main() -> int:
    text = ENTRY.strip()
    error = validate(text)
    if error is not None:
        print(error, file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
