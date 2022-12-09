#!/usr/bin/python3
# Advent of Code, Dec 02.
# https://adventofcode.com/2022/day/2
# J.Christensen 02Dec2022

import sys

def main() -> None:
    print("\n----PYTHON----")
    # R=1 P=2 S=3 Win=6 Draw=3 Lose=6
    score = { "R R" : 1+3, "R P" : 2+6, "R S" : 3+0, \
              "P R" : 1+0, "P P" : 2+3, "P S" : 3+6, \
              "S R" : 1+6, "S P" : 2+0, "S S" : 3+3 }
    tr1 = { 'A':'R', 'B':'P', 'C':'S', 'X':'R', 'Y':'P', 'Z':'S' }
    tbl1 = ''.maketrans(tr1)

    lines = sys.stdin.readlines()
    total = 0

    for l in lines:
        l = l.strip()
        round = l.translate(tbl1)
        points = score[round]
        if (points):
            #print(round, points)
            total += points
        else:
            print(f"Error: {l}")
            sys.exit(1)

    print(f"The total score for Part 1 is {total}.")

#---- PART 2 ----#

# given the opponent's throw, this hash encodes whether we should
# play for win, lose or draw.
    strategy = { "R W" : "P", "R L" : "S", "R D" : "R", \
                 "P W" : "S", "P L" : "R", "P D" : "P", \
                 "S W" : "R", "S L" : "P", "S D" : "S" }
    tr2 = { 'A':'R', 'B':'P', 'C':'S', 'X':'L', 'Y':'D', 'Z':'W' }
    tbl2 = ''.maketrans(tr2)
    total = 0

    for l in lines:
        l = l.strip()
        # determine what we should play
        round = l.translate(tbl2)
        # replace the second code letter from the input with our throw
        throw = strategy[round]
        round = round[0:2] + throw
        # calculate points as in part 1.
        points = score[round]
        # test to make sure the lookup worked
        if (points):
            #print(round, points)
            total += points
        else:
            print(f"Error: {l}")
            sys.exit(1)

    print(f"The total score for Part 2 is {total}.")

if __name__ == '__main__':
    main()
