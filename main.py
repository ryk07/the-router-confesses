#!/usr/bin/env python3
"""The Router Confesses — one original line from a home Wi-Fi router.

Writes a single excuse (<=200 characters) to /output/entry.txt.
Stdlib only. Paths are absolute, never resolved from the working directory.
"""

import os

LINE = (
    "I dropped the connection the second the killer's mask came off "
    "\u2014 after three years as 'FBI Surveillance Van,' "
    "that reveal was mine."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text == text.strip() and "\n" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
