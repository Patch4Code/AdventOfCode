# Advent of Code 2023
# Tag 11: Cosmic Expansion

from time import perf_counter as pfc
from itertools import combinations

def read_puzzle(filename):
    with open(filename) as datei:
        return datei.read().split("\n")


def solve_part_1(puzzle):
    
    matrix = [list(row) for row in puzzle]
    expanded_universe =[]

    # Zeichen nebeneinander betrachten
    for i, line in enumerate(matrix): 
        expanded_universe.append(line)
        if all(char == '.' for char in line):
           expanded_universe.append(line)

    expanded_universe2 = [[] for line in expanded_universe]
    for col in range(len(expanded_universe[0])):
        for row in range(len(expanded_universe)):
            expanded_universe2[row].append(expanded_universe[row][col])
        for row in range(len(expanded_universe)):
            if expanded_universe[row][col] != '.':
                break
        else:
            for row in range(len(expanded_universe)):
                expanded_universe2[row].append(expanded_universe[row][col])

    element_list = []
    for i, line in enumerate(expanded_universe2):
        for j, char in enumerate(line):
            if char == '#':
                element_list.append((i,j))
                
                
    #print(element_list)
    all_combinations = list(combinations(element_list, 2))
    summe = 0
    for combination in all_combinations:
        x_difference = abs(combination[0][0] - combination[1][0])
        y_difference = abs(combination[0][1] - combination[1][1])
        summe += (x_difference+y_difference)

    return summe


def solve_part_2(puzzle):
    
    matrix = [list(row) for row in puzzle]
    
    # Zeichen nebeneinander betrachten
    empty_lines = []
    empty_cols = []
    
    for i, line in enumerate(matrix): 
        if all(char == '.' for char in line):
           empty_lines.append(i)
    
    for j, col in enumerate(range(len(matrix[0]))):
        for row in range(len(matrix)):
            if matrix[row][col] != '.':
                break
        else:
            empty_cols.append(j)

    element_list = []
    for i, line in enumerate(matrix):
        for j, char in enumerate(line):
            if char == '#':
                element_list.append((i,j))
                   
    all_combinations = list(combinations(element_list, 2))
    summe = 0
    for combination in all_combinations:
        
        x_difference = 0
        for element in empty_lines:
            if element in range(min(combination[0][0], combination[1][0]), max(combination[0][0], combination[1][0])):
                x_difference += 1000000 - 1
        x_difference += abs(combination[0][0] - combination[1][0])        
        
        y_difference = 0
        for element in empty_cols:
            if element in range(min(combination[0][1], combination[1][1]), max(combination[0][1], combination[1][1])):
                y_difference += 1000000 - 1
        y_difference += abs(combination[0][1] - combination[1][1])

        summe += (x_difference+y_difference)
        
    return summe


if __name__ == "__main__":
    puzzle = read_puzzle("day11.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print (f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")

