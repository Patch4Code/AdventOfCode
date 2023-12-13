# Advent of Code 2023
# Day 12: Hot Springs

from time import perf_counter as pfc
from itertools import product

def read_puzzle(filename):
    with open(filename) as datei:
        return datei.read().split("\n")


def solve_part_1(puzzle):
    
    summe = 0
    for line in puzzle:
        first_part = line.split()[0]
        second_part = tuple([int(element) for element in line.split()[1].split(",")])

        # get all combinations
        possible_characters = ['.', '#']
        replacement_options = product(*[possible_characters for _ in range(first_part.count('?'))])
        all_combinations = [''.join(combination) for combination in replacement_options]
        
        all_strings = []
        for combination in all_combinations:
            one_string = ""
            counter = 0
            for char in first_part:
                if char == '?':
                    one_string += combination[counter]
                    counter += 1
                else:
                    one_string += char
            all_strings.append(one_string)

        # get all valid combinations
        for combination in all_strings:
            broken_list = tuple([len(group) for group in combination.split('.') if group])
            if broken_list == second_part:
                summe += 1

    return summe


def solve_part_2(puzzle):
    return 0


if __name__ == "__main__":
    puzzle = read_puzzle("day12.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print (f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")

