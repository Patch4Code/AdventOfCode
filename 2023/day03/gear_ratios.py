# Advent of Code 2023
# Day 3: Gear Ratios

import re
from time import perf_counter as pfc

def read_puzzle(filename):
    with open(filename) as datei:
        return datei.read().split('\n')
    
"""
Part 1:
Help an Elf fix a gondola lift by finding a missing engine part.
The engine schematic contains numbers and symbols, and adjacent numbers to symbols 
are considered "part numbers." Calculate the sum of all part numbers.
"""
def solve_part_1(puzzle):

    summe = 0

    for i, line in enumerate(puzzle):
        
        # returns list with tuples of numbers and their indexes --> e.g.: [(467, 0), (114, 5)]
        numbers_in_line = extract_numbers_from_line(line)
        
        # Iterate over each extracted number in the line
        for number in numbers_in_line:
            num_start, num_end = number[1], number[1]+len(str(number[0]))
            
            # Check for symbols in the current line and neighboring lines
            current_line_has_symbol = has_symbol_in_rang(line, max(0, num_start-1), min(len(line), num_end+1))
            above_line_has_symbol = i > 0 and has_symbol_in_rang(puzzle[i-1], max(0, num_start-1), min(len(puzzle[i-1]), num_end+1))
            below_line_has_symbol = i < len(puzzle)-1 and has_symbol_in_rang(puzzle[i+1], max(0, num_start-1), min(len(puzzle[i+1]), num_end+1))

            # If a symbol is found, add the corresponding number to the sum
            if current_line_has_symbol or above_line_has_symbol or below_line_has_symbol:
                summe += number[0]

    return summe


# Check if any symbol from the predefined set is present in the specified range of the line
def has_symbol_in_rang(line_to_check, start, end):
    symbols = "*-+/=%#&@!$?^~"
    substring = line_to_check[start:end]
    return any(char in symbols for char in substring) # any() returns True if any element of the iterable is true



"""
Part 2:
After fixing the missing part, the gondola still moves slowly due to a gear issue. 
Gears are any '*' symbol, that is adjacent to exactly two part numbers. 
Their gear ratio is the product of these two numbers. 
Calculate and sum all gear ratios to identify the faulty gear.
"""
def solve_part_2(puzzle):

    summe = 0

    for i, line in enumerate(puzzle):
        numbers_current_line = extract_numbers_from_line(puzzle[i])
        numbers_next_line = extract_numbers_from_line(puzzle[i+1]) if i < len(puzzle)-1 else []
        numbers_previous_line = extract_numbers_from_line(puzzle[i-1]) if i > 0 else []

        for j, char in enumerate(line):
            if char == "*":
                adjecent_numbers = []
                #search before star
                if j > 0:
                    for number in numbers_current_line:
                        if number[1]+len(str(number[0])) == j:
                            adjecent_numbers.append(number[0])
                #search behind star
                if j < len(line)-1:
                    for number in numbers_current_line:
                        if number[1] == j+1:
                            adjecent_numbers.append(number[0])
                #search below star
                if i < len(puzzle)-1:
                    for number in numbers_next_line:
                        number_range = set(range(number[1], number[1]+len(str(number[0]))))
                        star_range = set(range(j-1, j+2))
                        # --> & is the set intersection operator
                        if number_range & star_range:                                           
                            adjecent_numbers.append(number[0])
                #search above star
                if i > 0:
                    for number in numbers_previous_line:
                        number_range = set((range(number[1], number[1]+len(str(number[0])))))
                        star_range = set(range(j-1, j+2))
                        if number_range & star_range:                                                                 
                            adjecent_numbers.append(number[0])

                if len(adjecent_numbers) == 2:
                    summe += (adjecent_numbers[0] * adjecent_numbers[1])
    
    return summe


# Function to extract numbers and their positions from a line using regular expressions
def extract_numbers_from_line(line):
    # Find all matches of digits in the line
    matches = re.finditer(r'\d+', line)

    # Extract raw numbers and their indexes
    numbers_raw = [match.group() for match in matches]                  # match.group() returns the string matched by the RE 
    indexes = [match.start() for match in re.finditer(r'\d+', line)]    # match.start() returns the starting position of the match

    # Combine numbers and indexes into tuples
    numbers = [(int(numbers_raw[j]), indexes[j]) for j in range(len(numbers_raw))]

    return numbers


if __name__ == "__main__":
    puzzle = read_puzzle("day03.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print (f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
