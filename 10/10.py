#!/usr/bin/python3
# Day 10: Cathode-Ray Tube
# https://adventofcode.com/2022/day/10
# J.Christensen 10Dec2022

import pprint
import os
import re
import sys

def main() -> None:
    print(f"\n---- PYTHON {os.path.basename(__file__)} ----")

    # read the input, strip leading/trailing whitespace including newlines
    lines = sys.stdin.readlines()

    p1, p2 = solve(lines)
    print('AoC 2022 Day 10 Part 1:', p1)
    print('\nAoC 2022 Day 10 Part 2:\n')
    for l in p2:
        print(l)
    print()

def solve(lines: list) -> list:
    cpu = Machine(lines)
    clk = 0
    x = 1
    state = 'fetch'
    sum = 0
    interestingSS = 20  # cycles with interesting signal strength
    crtPixel = 0
    screenLine = ''
    screen = []

    while (True):
        if   (state == 'fetch'):        # fetch the next instruction
            if (cpu.hasMoreInst()):
                op, arg = cpu.fetch()
                if (op == 'noop'):
                    state = 'nop'
                else:
                    state = 'add1'
            else:
                break

        else:                           # execute the instruction
            clk += 1

            # calculations for part 1
            if (clk == interestingSS):
                sum += clk * x
                interestingSS += 40

            # calculations for part 2
            if (crtPixel >= x-1 and crtPixel <= x+1):
                screenLine += '#'
            else:
                screenLine += '.'
            crtPixel += 1
            if (crtPixel >= 40):
                screen.append(screenLine)
                crtPixel = 0
                screenLine = ''

            # execute the instruction
            if   (state == 'nop'):
                state = 'fetch'

            elif (state == 'add1'):
                state = 'add2'

            elif (state == 'add2'):
                x += arg
                state = 'fetch'

    return [sum, screen]

class Machine:
    def __init__(self, pgm: list) -> None:
        self.pgm = pgm
        self.ic = 1

    def fetch(self) -> list:
        inst = self.pgm[self.ic-1]
        f = inst.strip().split()
        op = f[0]
        if (op == 'addx'):
            arg = int(f[1])
        else:
           arg = ''
        self.ic += 1
        return [op, arg]

    def hasMoreInst(self) -> bool:
        return self.ic <= len(self.pgm)

if __name__ == '__main__':
    main()
