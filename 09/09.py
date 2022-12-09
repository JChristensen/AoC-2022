#!/usr/bin/python3
# Day 9: Rope Bridge
# https://adventofcode.com/2022/day/9
# J.Christensen 09Dec2022

import pprint
import os
import re
import sys

def main() -> None:
    print(f"\n---- PYTHON {os.path.basename(__file__)} ----")

    # read the input, strip leading/trailing whitespace including newlines
    lines = sys.stdin.readlines()

    # build the tree height array
    x = 0
    y = 0
    xMax = 0
    yMax = 0
    xMin = 0
    yMin = 0
    for l in lines:
        f = l.strip().split()
        dir = f[0]
        n = int(f[1])
        if (dir == 'L'):
            x -= n
        elif (dir == 'R'):
            x += n
        elif (dir == 'U'):
            y -= n
        elif (dir == 'D'):
            y += n
        xMax = max(x, xMax)
        yMax = max(y, yMax)
        xMin = min(x, xMin)
        yMin = min(y, yMin)
        print(dir, n, x, y, xMin, yMin, xMax, yMax)

if __name__ == '__main__':
    main()
