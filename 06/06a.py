#!/usr/bin/python3
# Day 6: Tuning Trouble
# https://adventofcode.com/2022/day/6
# J.Christensen 06Dec2022

import os
import pprint
import re
import sys

def main() -> None:
    print(f"\n---- PYTHON {os.path.basename(__file__)} ----")

    # read the input, strip leading and trailing whitespace including newlines
    buf = sys.stdin.read().strip()

    print("Part One", search(buf, 4))
    print("Part Two", search(buf, 14))

def search(s: str, n: int) -> int:
    """given string s, returns the position of the first substring of
    length n where all the characters in the substring are different.
    """
    for i in range(len(s) - n + 1):
        sss = s[i : i + n]    # a Sliding SubString of length n
        d = {}
        for c in sss:
            if (c not in d.keys()):
                d[c] = 1
            else:
                d[c] += 1
        if (len(d.keys()) == n):
            break
    return i + n

if __name__ == '__main__':
    main()
