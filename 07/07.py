#!/usr/bin/python3
# Day 7: No Space Left On Device
# https://adventofcode.com/2022/day/7
# J.Christensen 07Dec2022

import pprint
import os
import re
import sys

def main() -> None:
    print(f"\n---- PYTHON {os.path.basename(__file__)} ----")

    # read the input, strip leading/trailing whitespace including newlines
    lines = sys.stdin.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    print('AoC 2022 Day 07 Part 1:', partOne(lines))
    print('AoC 2022 Day 07 Part 2:', partTwo())

def partOne(lines: list) -> int:
    t = {'/':{}}    # the file system tree
    cwd = {}        # the current working directory
    d = []          # the cwd as a list of directory names

    for l in lines:
        f = l.split()
        if (f[0] == '$' and f[1] == 'cd'):
            if (f[2] == '..'):
                del d[-1]
                cwd = {}
                for n in d:
                    if (n == '/'):
                        cwd = t[n]
                    else:
                        cwd = cwd[n]
            else:
                d.append(f[2])
                cwd = {}
                for n in d:
                    if (n == '/'):
                        cwd = t[n]
                    else:
                        cwd = cwd[n]
        elif (f[0] == 'dir'):
            cwd[f[1]] = {}
        elif (f[0].isdecimal()):
            cwd[f[1]] = int(f[0])
        elif (f[0] == '$' and f[1] == 'ls'):
            pass

    dirSize('', t)
    total = 0
    for k, v in dirlist.items():
        if (v <= 100000):
            total += v
    return total 

def dirSize(parent: str, t: dict) -> int:
    total = 0
    for k, v in t.items():
        if (type(v) == type({})):
            if (k == '/'):
                path = k
            else:
                path = parent + k + '/'
            s = dirSize(path, v)
            dirlist[path] = s
            total += s
        else:
            total += v

    return total

def partTwo() -> int:
    total = 70000000
    needed = 30000000
    used = dirlist['/']
    unused = total - used
    mustFree = needed - unused

    # build a dictionary of directories that are large enough
    candidates = {}
    for k, v in dirlist.items():
        if (v >= mustFree):
            candidates[k] = v
    return min(candidates.values())

global dirlist
dirlist = {}
if __name__ == '__main__':
    main()
