#!/usr/bin/env python3
"""Worst Superpower — make.fun bounty u-suroto-worst-superpower-461dcdbe.

Writes one line (at most 140 characters) inventing the most useless
superpower to entry.txt. Pure Python stdlib, no network, reads nothing
outside the repo.

Final line: "I can read minds — but only my own, and only the thoughts
I've already had." It beats the draft ("I can predict the future — but
only events that already happened yesterday"): predicting yesterday is
a familiar time-travel gag, while reading your own already-had thoughts
is a power that achieves literally nothing — no curse, no hidden help,
just a mind-reader whose only subject already knows everything he
"discovers". The redundancy is the whole joke, and it lands on one
reading with a concrete, specific image.
"""

import os
from pathlib import Path

ENTRY = "I can read minds — but only my own, and only the thoughts I've already had."


def main() -> None:
    assert isinstance(ENTRY, str)
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, must be 1-140"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"

    out_dir = os.environ.get("OUTPUT_DIR") or os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} chars to {out_path}")


if __name__ == "__main__":
    main()
