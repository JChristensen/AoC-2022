#!/usr/bin/python3
# Day 8: Treetop Tree House
# https://adventofcode.com/2022/day/8
# J.Christensen 08Dec2022

import pprint
import os
import re
import sys

def main() -> None:
    print(f"\n---- PYTHON {os.path.basename(__file__)} ----")
    global h        # array of tree heights
    global v        # array of visible trees
    global nRows
    global nCols

    # read the input, strip leading/trailing whitespace including newlines
    lines = sys.stdin.readlines()

    # build the tree height array
    h = []
    for l in lines:
        l = l.strip()
        row = []
        for c in l:
            row.append(int(c))
        h.append(row)

    nRows = len(h)
    nCols = len(h[0])
    v = zeroMatrix() 
    print('AoC 2022 Day 08 Part 1:', partOne())
    v = zeroMatrix() 
    print('AoC 2022 Day 08 Part 2:', partTwo())

def partTwo() -> int:
    for tr in range(1, nRows-1):        # row of the tree we're inspecting (tree row)
        for tc in range(1, nCols-1):    # col of the tree we're inspecting (tree col)
            th = h[tr][tc]              # height of the tree we're inspecting

            # looking east
            east = 0
            for c in range(tc+1, nCols):
                if (h[tr][c] >= th or c == nCols-1):
                    east += c - tc
                    break

            # looking south
            south = 0
            for r in range(tr+1, nRows):
                if (h[r][tc] >= th or r == nRows-1):
                    south += r - tr
                    break

            # looking west
            west = 0
            for c in range(tc-1, -1, -1):
                if (h[tr][c] >= th or c == 0):
                    west += tc - c
                    break

            # looking north
            north = 0
            for r in range(tr-1, -1, -1):
                if(h[r][tc] >= th or r == 0):
                    north += tr - r
                    break

            v[tr][tc] = north * east * south * west

    maxScenic = 0
    for r in v:
        for c in r:
            maxScenic = max(c, maxScenic)
    return maxScenic

def partOne() -> int:
    # looking east
    for r in range(nRows):
        tallest = -1
        for c in range(nCols):
            if (h[r][c] > tallest):
                tallest = h[r][c]
                v[r][c] = 1

    # looking south
    for c in range(nCols):
        tallest = -1
        for r in range(nRows):
            if (h[r][c] > tallest):
                tallest = h[r][c]
                v[r][c] = 1

    # looking west
    for r in range(nRows):
        tallest = -1
        for c in range(nCols-1, -1, -1):
            if (h[r][c] > tallest):
                tallest = h[r][c]
                v[r][c] = 1

    # looking north
    for c in range(nCols):
        tallest = -1
        for r in range(nRows-1, -1, -1):
            if (h[r][c] > tallest):
                tallest = h[r][c]
                v[r][c] = 1

    total = 0
    for r in v:
        for c in r:
            total += c
    return total

def zeroMatrix() -> list:
    m = []
    for r in range(nRows):
        m.append([])
        for c in range(nCols):
            m[r].append(0)
    return m

def printMatrix(m: list) -> None:
    print()
    for r in m:
        for c in r:
            print(c, end='')
        print()

if __name__ == '__main__':
    main()
