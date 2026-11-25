#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note.

Writes one line of patch notes to /output/entry.txt.
Deterministic, offline, standard library only.
"""

ENTRY = "Fixed: the sleep tracker no longer wakes you at 3 a.m. to report that you are not sleeping."


def main():
    import os

    # Gate: one line, 1-160 characters, not only whitespace.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 160, "entry must be 1-160 characters"
    assert text and not text.isspace()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
