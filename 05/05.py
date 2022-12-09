#!/usr/bin/python3
# Day 5: Supply Stacks
# https://adventofcode.com/2022/day/5
# J.Christensen 05Dec2022

import pprint
import os
import re
import sys

def main() -> None:
    print(f"\n---- PYTHON {os.path.basename(__file__)} ----")

    # read the input, strip trailing whitespace including newlines
    lines = sys.stdin.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()

    print('The top crates for Part One are:', moveCrates(lines, 9000))
    print('The top crates for Part Two are:', moveCrates(lines, 9001))

def moveCrates(lines: list, craneModel: int) -> str:
    if (craneModel < 9000 or craneModel > 9001):
        print('Invalid crane model!', file=sys.stderr)
        sys.exit(1)

    # determine number of stacks, and height of tallest stack
    height = 0
    nstack = 0
    for l in lines:
        f = l.split()
        if (f[0] == "1"):
            nstack = int(f[-1])
            break
        height += 1

    # build the stacks
    stacks = []
    for s in range(nstack):
        stacks.append([])

    for l in range(height-1, -1, -1):
        for s in range(nstack):
            charIndex = s * 4 + 1
            if (charIndex <= len(lines[l])):
                crate = lines[l][charIndex]
                if (crate != ' '):
                    stacks[s].append(crate)
    #pprint.pprint(stacks, compact=True, width=120)

    # start up the crane
    for l in lines:
        if (l[0:4] == 'move'):
            f = l.split()
            n = int(f[1])
            # silly elves index from one not zero, so subtract 1.
            src = int(f[3]) - 1
            dest = int(f[5]) - 1
            #print('\n', f, n, src, dest)
            if (craneModel == 9000):
                for c in range(n):
                    stacks[dest] += stacks[src][-1:]
                    stacks[src] = stacks[src][:-1]
            elif (craneModel == 9001):
                stacks[dest] += stacks[src][-n:]
                stacks[src] = stacks[src][:-n]
            #pprint.pprint(stacks, compact=True, width=120)

    # make the result
    topcrates = ''
    for s in range(nstack):
        topcrates += stacks[s][-1]
    return topcrates

if __name__ == '__main__':
    main()
