#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse — make.fun entry.

Writes one excuse, from a robot vacuum explaining why it missed a
spot, to /output/entry.txt. Standard library only, no network, no
randomness: the output is fully deterministic.
"""

import os

# One line, 98 characters. The vacuum owns the failure in its own
# voice — suction quit, wheels gave up — then the missed crumb gets
# the punchline: it filed for squatter's rights, so it lives here
# now. Pure vacuum world (suction, wheels, crumbs, the floor it
# patrols), a real joke, and no setup the reader has to supply.
LINE = "My suction quit, my wheels gave up, and that crumb filed for squatter's rights. It lives here now."


def validate_entry(text):
    """The gate allows UTF-8 text of 1 to 120 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not (1 <= len(text) <= 120):
        raise ValueError("entry must be 1 to 120 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    entry = validate_entry(LINE)
    # ENTRY_OUTPUT is honoured so the entry can be verified locally
    # without touching /output; the sandbox run uses the default.
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    # Self-check gate: re-read the file and assert it holds exactly
    # the validated line, byte for byte. The output is unchanged.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == entry, "entry.txt does not match the validated line"
    assert 1 <= len(written) <= 120, "entry.txt must be 1 to 120 characters"
    assert written.strip(), "entry.txt must not be only whitespace"


if __name__ == "__main__":
    main()
