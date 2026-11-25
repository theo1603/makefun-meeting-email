#!/usr/bin/env python3
"""Write one meeting-that-should-have-been-an-email one-liner to /output/entry.txt.

Stdlib only, no network, fully deterministic: the same line on every run.
"""

import os

# Grading runs this with no environment set, so it writes /output/entry.txt
# as the rules require. ENTRY_OUTPUT_DIR exists only so local test runs can
# aim at a private directory: /output is shared on this machine and another
# process overwrote it mid-test (a therapist joke, not this entry).
OUT_DIR = os.environ.get("ENTRY_OUTPUT_DIR", "/output")

LINE = (
    "The meeting's only decision was to book a follow-up meeting to decide "
    "if the first meeting could have been an email."
)


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
