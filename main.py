#!/usr/bin/env python3
"""The Funniest Honest Appliance Error.

Writes one line -- the funniest honest error message a washing machine
could show -- to /output/entry.txt.

The line: an overdosed detergent fault. The machine did its job (the
clothes are clean) and failed at the same time (the foam escaped onto
the floor). Flat machine voice, no explaining of the joke.
"""

import os
import shutil

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

ENTRY = (
    "ERROR: Too much detergent. "
    "The drum is full of foam. "
    "Your clothes are clean. "
    "The floor is not."
)


def clean_output_dir() -> None:
    """Remove only the contents of the output folder, never the folder."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)


def main() -> None:
    # The gate rejects anything outside 1-200 chars or blank-only text.
    # Fail loudly here rather than shipping an entry that can never be judged.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit("entry line fails the 1-200 char gate: %d chars" % len(ENTRY))
    clean_output_dir()
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
