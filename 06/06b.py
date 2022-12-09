#!/usr/bin/python3
# Day 6: Tuning Trouble
# https://adventofcode.com/2022/day/6
# H/T https://github.com/SnoozeySleepy/AdventOfCode2022/blob/main/day6.py
# J.Christensen 06Dec2022

import os
import pprint
import re
import sys

def main() -> None:
    print(f"\n---- PYTHON {os.path.basename(__file__)} ----")

    # read the input, strip leading and trailing whitespace including newlines
    buf = sys.stdin.read().strip()

    print("Part One packet start at ", search(buf, 4))
    print("Part Two message start at", search(buf, 14))

def search(s: str, n: int) -> int:
    """given string s, returns the position of the first substring of
    length n where all the characters in the substring are different.
    """
    for i in range(len(s) - n + 1):
        sss = s[i : i + n]    # a Sliding SubString of length n
        if (len(set(sss)) == n):
            return i + n

if __name__ == '__main__':
    main()
