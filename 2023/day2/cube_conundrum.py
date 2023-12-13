# Advent of Code 2023
# Day 2: Cube Conundrum

from time import perf_counter as pfc

def read_puzzle(filename):
    with open(filename) as file:
        
        # Initialize the puzzle input list
        puzzleinput_list = [
            [   
                [color.strip() for color in color_sublist.split(',')] 
                for color_sublist in line.split(':')[1].split(';') # iterate over all color_sublists (cubes) separated by ';'
            ]
            for line in file.read().split('\n') # iterate over all lines of input
        ]
        
        #new list_format: [[['3 blue', '4 red'], ['1 red', '2 green', '6 blue'], ['2 green']], ...
        return puzzleinput_list


"""
On Snow Island, an Elf invites you to a cube game.
The bag contains red, green, and blue cubes, with random subsets revealed in each game. 
Identify possible games if the bag initially had 12 red, 13 green, and 14 blue cubes. Calculate the sum of their IDs.
"""
def solve_part_1(puzzle):
    cube_map = {"red": 12, "green": 13, "blue": 14,}
    summe = 0 

    # iterate over all lines of the puzzle with a counter representing the id of the line
    for id, line in enumerate(puzzle, start=1):
        
        # all() returns True if all elements of the iterable are true --> iterate over all color sets of the line and 
        # check if all elements of the color_set are smaller or equal to the corresponding value in the cube_map 
        if all(int(element.split()[0]) <= cube_map.get(element.split()[1]) for color_set in line for element in color_set):
            summe += id

    return summe


"""
As you continue to walk, the Elf poses a second question: 
for each game, determine the minimum cubes needed for each color to make the game possible. 
Calculate the sum of the powers (numbers of red, green, and blue cubes multiplied together) of these minimum cube sets.
"""
def solve_part_2(puzzle):

    result = 0
    for line in puzzle:
        cube_map = {"red": 0, "green": 0, "blue": 0,}

        for color_set in line: 
            for element in color_set:
                # tempory save of color and amount of the element
                color, amount = element.split()[1], int(element.split()[0])
                
                # Update cube_map entry for given color with the maximum value of current amount and value in cube_map
                cube_map[color] = max(cube_map[color], amount)
                    
        product = 1
        for key in cube_map: product *= cube_map[key]
        result += product          
    
    return result


if __name__ == "__main__":
    puzzle = read_puzzle("day02.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print (f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")