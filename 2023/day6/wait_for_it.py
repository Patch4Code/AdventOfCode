# Advent of Code 2023
# Day 6: Wait For It

import re
import math
from time import perf_counter as pfc

def read_puzzle(filename):
    with open(filename) as datei:
        return datei.read().split('\n')


def solve_part_1(puzzle):
    times = list(map(int, puzzle[0].split(":")[1].strip().split()))
    distance_records = list(map(int, puzzle[1].split(":")[1].strip().split()))

    #go over each race
    result = 1
    for i, time in enumerate(times):
        nums_to_win = 0
        for j in range(0, distance_records[i]+1):
            if(j*(time - j) > distance_records[i]):
                nums_to_win += 1
        result *= nums_to_win  
    
    return result


def solve_part_2(puzzle):
    time = int(puzzle[0].replace(" ", "").split(":")[1])
    distance_record = int(puzzle[1].replace(" ", "").split(":")[1])
    
    nums_to_win2 = 0
    for j in range(time):
        if(j*(time - j) > distance_record):
            nums_to_win2 += 1

    return nums_to_win2


if __name__ == "__main__":
    puzzle = read_puzzle("day06.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print (f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")

