#!/usr/bin/python3
# Day 12: Hill Climbing Algorithm
# https://adventofcode.com/2022/day/12
# J.Christensen 12Dec2022

import pprint
import os
import re
import sys

def main() -> None:
    print(f"\n---- PYTHON {os.path.basename(__file__)} ----")

    # read the input
    lines = sys.stdin.readlines()

    solve(lines)
    #print('AoC 2022 Day 12 Part 1:')

def solve(lines: list) -> None:
    g = Graph()
    xmax = len(lines[0].strip())
    ymax = len(lines)
    y = 0
    # add vertices
    for l in lines:
        x = 0
        for c in l.strip():
            v = str(x) + ',' + str(y)   # vertex name (key)
            if (c == 'S'):
                start = v
                c = 'a'
            elif (c == 'E'):
                end = v
                c = 'z'
            g.addVertex(v, ord(c)-96)
            x += 1
        y += 1

    # add edges
    for y in range(ymax):
        for x in range(xmax):
            for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                dx = d[0]
                dy = d[1]
                if (x+dx >= 0 and x+dx < xmax and y+dy >=0 and y+dy < ymax):
                    v = str(x) + ',' + str(y)
                    e = str(x+dx) + ',' + str(y+dy)
                    if (g.getValue(e) <= g.getValue(v) + 1):
                        g.addEdge(v, e)

    gr = g.getGraph()
    visited = [start]
    queue = [start]
    parent = {}
    parent[start] = None
    while (len(queue) > 0):
        v = queue.pop(0)
        if (v == end):
            break
        for e in gr[v][1]:
            if (e not in visited):
                queue.append(e)
                visited.append(e)
                parent[e] = v

    v = end
    path = []
    while(v != start):
        path.append(v)
        v = parent[v]
    print(len(path), path)

class Graph:
    def __init__(self) -> None:
        self.g = {}

    def addVertex(self, v: str, val: int) -> None:
        self.g[v] = [val, []]

    def addEdge(self, v: str, e: str) -> None:
        self.g[v][1].append(e)
    
    def getValue(self, v: str) -> int:
        return self.g[v][0]

    def getGraph(self) -> dict:
        return self.g

if __name__ == '__main__':
    main()
