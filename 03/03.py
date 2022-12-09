#!/usr/bin/python3
# Rucksack Reorganization.
# Advent of Code, Dec 03.
# https://adventofcode.com/2022/day/3
# J.Christensen 03Dec2022

import os
import sys

def main() -> None:
    print(f"\n---- PYTHON {os.path.basename(__file__)} ----")

    # read the input, strip leading/trailing whitespace including newlines
    lines = sys.stdin.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    #---- PART ONE ----#
    total = 0
    for l in lines:
        # number of items in one compartment
        n = len(l) // 2
        # make the first and second compartment lists
        c1 = l[:n]
        c2 = l[-n:]

        # find the duplicate item, calculate and accumulate the priority
        for r in range(n):
            if (c1[r] in c2):
                item = c1[r]
                total += priority(item)
                break

    print(f"The sum of priorities for Part 1 is {total}.")

    #---- PART TWO ----#
    total = 0
    for r in range(0, len(lines), 3):       # three elves at a time
        for i in range(0, len(lines[r])):   # iterate each character for the first elf
            item = lines[r][i]
            if (item in lines[r+1] and item in lines[r+2]):
                total += priority(item)
                break

    print(f"The sum of priorities for Part 2 is {total}.")

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
def priority(ch: str) -> int:
    return ord(ch) - 96 if ord(ch) > 96 else ord(ch) - 64 + 26

if __name__ == '__main__':
    main()
