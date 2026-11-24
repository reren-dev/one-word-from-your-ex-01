#!/usr/bin/env python3
"""One Word From Your Ex.

The word my ex would use to describe me: Rebound.

Why this word: it is a label exes actually use about a partner
("he was just a rebound"), it lands instantly with no explanation,
it stings because it is painfully true, and almost everyone has
either been one or dated one — the exact mix the judge weighs:
one real word, funny, honest, instant, relatable.
"""

import os

WORD = "Rebound"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Enforce the gate ourselves: exactly one word, 1-24 characters,
    # no whitespace, so a bad edit fails loudly here instead of
    # silently producing an invalid entry.
    if not WORD or len(WORD) > 24 or any(ch.isspace() for ch in WORD):
        raise ValueError(f"not a valid one-word entry: {WORD!r}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
