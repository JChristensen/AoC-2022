#!/usr/bin/python3
# Advent of Code, Dec 01.
# https://adventofcode.com/2022/day/1
# J.Christensen 01Dec2022

import sys

def main() -> None:
    lines = sys.stdin.readlines()
    cal = 0;        # total calories for current elf
    elves = [];     # a list of total calories for all elves

    for l in lines:
        l = l.strip()
        if (len(l) == 0):
            elves.append(cal)
            cal = 0
        else:
            cal += int(l)

    if (cal > 0):
        elves.append(cal)

    elves.sort(reverse=True)
    topThree = elves[0] + elves[1] + elves[2]
    print(f"There are {len(elves)} elves.")
    print(f"The most calories an elf has is {elves[0]}.")
    print(f"The top three elves have a total of {topThree} calories.")

if __name__ == '__main__':
    main()
