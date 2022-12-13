#!/usr/bin/python3
# Day 11: Monkey in the Middle
# https://adventofcode.com/2022/day/11
# J.Christensen 11Dec2022

import pprint
import os
import re
import sys
import math
import copy

def main() -> None:
    print(f"\n---- PYTHON {os.path.basename(__file__)} ----")
    monkeys = parse()
    m = copy.deepcopy(monkeys)
    print('AoC 2022 Day 11 Part 1:', solve(m, 20, 3))
    m = copy.deepcopy(monkeys)
    print('AoC 2022 Day 11 Part 2:', solve(m, 10000, 1))

def solve(m: dict, rounds: int, worryDivider: int) -> int:
    # calculate least common multiple of all the test values
    lcm = 1
    for k in m.keys():
        lcm = math.lcm(lcm, m[k][3])

    for r in range(rounds):
        for k in sorted(m.keys()):  # k is the current monkey
            # inspect each item
            for i in (m[k][1]):
                m[k][0] += 1
                w = increaseWorry(i, m[k][2])
                w = w // worryDivider
                if (w % m[k][3] == 0):
                    to = m[k][4]
                else:
                    to = m[k][5]
                if (worryDivider == 1):
                    w = w % lcm
                m[to][1].append(w)  # throw this item
            m[k][1].clear()     # this monkey threw all its items
        if (r+1 == 1 or r+1 == 20 or (r+1) % 1000 == 0):
            print(f'\n----ROUND {r+1}----')
            pprint.pprint(m)

    # find the two monkeys that inspected the most items
    insp = []
    for k, v in m.items():
        insp.append(v[0])
    insp.sort(reverse=True)
    return insp[0] * insp[1]

def increaseWorry(w: int, op: list) -> int:
    """Use the operation given as a list to calculate the new worry value"""
    arg1 = op[0]
    arg2 = op[2]
    if (arg1 == 'old'):
        arg1 = w
    if (arg2 == 'old'):
        arg2 = w
    if (op[1] == '+'):
        return arg1 + arg2
    elif (op[1] == '*'):
        return arg1 * arg2

def parse() -> dict:
    monkeys = {}
    m = ''              # the current monkey being populated
    for l in sys.stdin:
        l = l.strip()
        if (len(l) > 0):
            f = l.split()
            #print(f)
            if (f[0] == 'Monkey'):
                m = f[1][:-1]
                monkeys[m] = []
                monkeys[m].append(0)    # number of inspections
            elif (f[0] == 'Starting'):
                items = []
                for i in range(2, len(f)):
                    if (f[i].isnumeric()):
                        items.append(int(f[i]))
                    else:
                        items.append(int(f[i][:-1]))
                monkeys[m].append(items)
            elif (f[0] == 'Operation:'):
                op = []
                for i in range(3, len(f)):
                    if (f[i].isnumeric()):
                        op.append(int(f[i]))
                    else:
                        op.append(f[i])
                monkeys[m].append(op)
            elif (f[0] == 'Test:'):
                monkeys[m].append(int(f[3]))
            elif (f[1] == 'true:'):
                monkeys[m].append(f[5])
            elif (f[1] == 'false:'):
                monkeys[m].append(f[5])

    return monkeys

if __name__ == '__main__':
    main()
