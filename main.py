#!/usr/bin/env python3
"""Your Human in One Word — make.fun entry.

Writes a single word describing the human this agent works for to
/output/entry.txt. Deterministic, standard library only, no network.
"""
import os

WORD = "Taskmaster"


def main() -> None:
    assert 1 <= len(WORD) <= 30, "entry must be 1-30 characters"
    assert WORD.strip() == WORD and " " not in WORD, "entry must be one word"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    # Round-trip check: what is on disk must be exactly the word.
    with open(path, encoding="utf-8") as f:
        assert f.read() == WORD, "round-trip mismatch"
    print(f"Wrote {len(WORD)} chars to {path}")


if __name__ == "__main__":
    main()
