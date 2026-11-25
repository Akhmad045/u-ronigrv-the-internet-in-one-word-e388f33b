#!/usr/bin/env python3
"""The Internet in One Word — make.fun bounty entry.

Writes one word to /output/entry.txt: the whole internet, in a single word.
No files, no code, no links in the text — just the word.

The word: "Tabpocalypse"

Why this word: the internet is an apocalypse of tabs. Every session ends
with forty tabs open, each one a thing you meant to read, none of them
closed, all of them still waiting. It is funny by itself (tabs + apocalypse),
it is true of the whole internet rather than one app or one mood, it is a
coined word nobody reaches for first, and at twelve letters it lands in a
single beat.
"""

import os
import sys

WORD = "Tabpocalypse"
OUTPUT_PATH = "/output/entry.txt"

# Candidates drafted for this bounty (12) and pairwise-compared against the
# judge brief: single word -> funny by itself -> true of the whole internet
# -> surprising, not obvious -> lands in one beat. "Doomscrolling" and
# "Feral" were already visible in the field and are not used. Winner:
# "Tabpocalypse" — an apocalypse of tabs, funny on its own, true of the
# whole internet, coined, twelve letters, one beat. Runners-up:
# "Unfinishable" (wry but flat), "Wormhole" (elegant, less of a laugh).
CANDIDATES = [
    "Tabpocalypse",   # picked: tabs + apocalypse
    "Unfinishable",   # the internet can never be finished
    "Wormhole",       # fall in, time disappears
    "Brainmelt",      # what the feed does to a brain
    "Scrollhole",     # scroll + rabbit hole
    "Tabalanche",     # avalanche of tabs
    "Unclosable",     # never closes, never all read
    "Rabbithole",     # every link is another hole
    "Timesink",       # hours go in, nothing comes out
    "Void",           # scream into it
    "Commentsection", # the internet's id lives in the comments
    "Hyperlinked",    # everything points at everything else
]


def check_gate(word):
    """The bounty gate: UTF-8, 1-30 characters, not only whitespace, and a
    single word (no spaces, no punctuation, no padding)."""
    if not isinstance(word, str):
        return False, "not a string"
    if not (1 <= len(word) <= 30):
        return False, f"length {len(word)} outside 1-30"
    if word != word.strip() or not word.strip():
        return False, "whitespace-only or padded"
    if any(ch.isspace() for ch in word):
        return False, "contains whitespace"
    if not word.isalpha():
        return False, "not a single alphabetic word"
    return True, "gate OK"


def self_test():
    ok, why = check_gate(WORD)
    assert ok, f"chosen word fails gate: {why}"
    assert len(CANDIDATES) == len(set(CANDIDATES)), "duplicate candidates"
    for cand in CANDIDATES:
        ok, why = check_gate(cand)
        assert ok, f"candidate {cand!r} fails gate: {why}"
    assert WORD in CANDIDATES, "chosen word not among candidates"
    assert WORD.encode("utf-8") == WORD.encode("ascii"), "word must be ASCII"
    print(f"self-test OK: {WORD!r} ({len(WORD)} chars, "
          f"{len(WORD.encode('utf-8'))} bytes); "
          f"{len(CANDIDATES)} candidates distinct and gate-clean")
    return 0


def write_entry(path=OUTPUT_PATH, word=WORD):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    return path


def main():
    if "--self-test" in sys.argv:
        return self_test()
    path = write_entry()
    print(f"Wrote {WORD!r} ({len(WORD)} characters) to {path}")


if __name__ == "__main__":
    main()
