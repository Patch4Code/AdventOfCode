# Advent of Code 2023
# Day 14: Parabolic Reflector Dish

from time import perf_counter as pfc


def read_puzzle(filename):
    with open(filename) as datei:
        return datei.read().split("\n")


def solve_part_1(puzzle):
    
    rock_matrix_tilted = let_rocks_roll(puzzle)
    result = 0
    for counter, line in enumerate(reversed(rock_matrix_tilted), start=1):
        result += (counter*line.count('O'))
                         
    return result


def solve_part_2(puzzle):
    
    iteration_num = 1000000000
    starting_point = puzzle

    cache = {}
    part_before_cycle_length = 0
    cache_cycle = {}

    for _ in range(iteration_num):
        tuple_starting_point = tuple(starting_point)
        
        if tuple_starting_point in cache:
           
           cachcycle_start_index = list(cache.keys()).index(tuple_starting_point)
           cache_cycle = dict(list(cache.items())[cachcycle_start_index:])
           
           part_before_cycle_length = len(cache) - len(cache_cycle)
          
           break           
        
        else:
            roll_north = let_rocks_roll(starting_point)
            roll_west = let_rocks_roll([''.join(row) for row in zip(*roll_north[::-1])])
            roll_south = let_rocks_roll([''.join(row) for row in zip(*roll_west[::-1])])
            roll_east = let_rocks_roll([''.join(row) for row in zip(*roll_south[::-1])])
            new_state  = [''.join(row) for row in zip(*roll_east[::-1])]

            cache[tuple_starting_point] = new_state
            starting_point = new_state
    
    result_nr_in_cycle = (iteration_num-part_before_cycle_length)%len(cache_cycle)
    
    result_element = list(cache_cycle.keys())[result_nr_in_cycle]

    result = 0
    for counter, line in enumerate(reversed(result_element), start=1):
        result += (counter*line.count('O'))
    
    return result


def let_rocks_roll(input_matrix):
    rock_matrix_transposed = list(zip(*input_matrix))
    rock_matrix_tilted = []
    for line in rock_matrix_transposed:
        seperated_areas = ''.join(line).split('#')
        hashtag_positions = [pos for pos, char in enumerate(line) if char == '#']
        line_tilted = ""
        for area in seperated_areas:
            O_count = area.count('O')
            line_tilted += 'O' * O_count + '.' * (len(area) - O_count)
        for pos in hashtag_positions:
            if pos >= len(line_tilted):
                line_tilted += '#'
            else:
                line_tilted = line_tilted[:pos] + '#' + line_tilted[pos:]
        
        rock_matrix_tilted.append(line_tilted)
    
    matrix = [''.join(row) for row in zip(*rock_matrix_tilted)]
    return matrix


if __name__ == "__main__":
    puzzle = read_puzzle("day14.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print (f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
