#!/usr/bin/python3
# Day 4: Camp Cleanup
# https://adventofcode.com/2022/day/4
# J.Christensen 04Dec2022

import os
import re
import sys

def main() -> None:
    print(f"\n---- PYTHON {os.path.basename(__file__)} ----")

    # read the input, strip leading/trailing whitespace including newlines
    lines = sys.stdin.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    # delimiters to split input
    reDelim = re.compile(r',|-')

    #---- PART ONE ----#
    total = 0
    # parse the fields; convert to integer
    for l in lines:
        f = re.split(reDelim, l)
        for i in range(len(f)):
            f[i] = int(f[i])
        min1 = min(f[0], f[1])
        max1 = max(f[0], f[1])
        min2 = min(f[2], f[3])
        max2 = max(f[2], f[3])
        if ( ((min1 >= min2) and (max1 <= max2)) or ((min2 >= min1) and (max2 <= max1)) ):
            total += 1
    print(f'Part 1 total {total}.')

    #---- PART TWO ----#
    total = 0
    # parse the fields; convert to integer
    for l in lines:
        f = re.split(reDelim, l)
        for i in range(len(f)):
            f[i] = int(f[i])
        min1 = min(f[0], f[1])
        max1 = max(f[0], f[1])
        min2 = min(f[2], f[3])
        max2 = max(f[2], f[3])
        if ( ((max1 >= min2) and (max1 <= max2)) or ((max2 >= min1) and (max2 <= max1)) ):
            total += 1
    print(f'Part 2 total {total}.')

if __name__ == '__main__':
    main()
