"""The Most Boring Object, Reviewed in One Line.

Writes one funny, true review of the dullest everyday object we could
name to /output/entry.txt. Deterministic: the same single line, every run.
"""

import os

ENTRY = (
    "The sponge soaks up everyone else's mess, smells like a crime scene "
    "by Friday, and still shows up for work on Monday."
)


def main() -> None:
    # Guard the gate: one line, 1-200 characters, never only whitespace.
    assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 200 and ENTRY.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
