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

    print('AoC 2022 Day 09 Part 1:', solve(2,  lines))
    print('AoC 2022 Day 09 Part 2:', solve(10, lines))

def solve(nKnots: int, lines: list) -> int:
    hMoves = {'L':[-1,0], 'R':[1,0], 'U':[0,1], 'D':[0,-1]}
    knots = []
    for i in range(nKnots):
        knots.append([0, 0])    # x and y coord of ten knots
    visited = {}    # points visited by tail, uses stringified points as keys, e.g. '1,2'

    for l in lines:
        f = l.strip().split()
        dir = f[0]
        n = int(f[1])

        for i in range(int(f[1])):
            knots[0] = move(knots[0], hMoves[f[0]])
            for j in range(1, nKnots):
                knots[j] = move(knots[j], tMove(knots[j-1], knots[j]))
            tStr = strPoint(knots[nKnots-1])
            visited.setdefault(tStr, 0)
            visited[tStr] += 1

    return len(visited.keys())

def tMove(p1: list, p2: list) -> list:
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    if (abs(dx) > 1 or abs(dy) > 1):
        if (dx == 2):
            dx = 1
        if (dx == -2):
            dx = -1
        if (dy == 2):
            dy = 1
        if (dy == -2):
            dy = -1
        return [dx, dy]
    else:
        return [0, 0]

def move(point: list, delta: list) -> list:
    result=[]
    result.append(point[0] + delta[0])
    result.append(point[1] + delta[1])
    return result

def strPoint(p: list) -> str:
    """stringify a point"""
    return str(p[0]) + ',' + str(p[1])

if __name__ == '__main__':
    main()
