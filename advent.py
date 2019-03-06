# Day 1 Advent of Code: Puzzle Input https://adventofcode.com/2018/day/1/input

from itertools import accumulate
from collections import Counter

def day1():
    orglist = open("input.txt")
    lines = orglist.readlines()
    total = 0
    newlist = []
    success = False

    while success is False:
        for line in lines:
            total = total + int(line)
            newlist.append(total)

        print(total)
        print(newlist)

        countlist = Counter(newlist)
        print(countlist)
        countlist = dict(countlist)

        for key, value in countlist.items():
            if value > 1:
                print(key, value)
                success = True

day1()