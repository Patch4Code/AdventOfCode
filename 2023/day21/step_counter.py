# Advent of Code 2023
# Day 19: Step Counter
from time import perf_counter as pfc


def read_puzzle(filename):
    with open(filename) as datei:
        return datei.read().split("\n")
    
def solve_part_1(puzzle):
    
    start_pos = next(((x, y) for y, line in enumerate(puzzle) for x, col in enumerate(line) if col == "S"), None)

    locations = {start_pos}
    for _ in range(64):
        new_locations = set()
        for x,y in locations:
            #north
            if y > 0 and puzzle[y-1][x] != "#":
                new_locations.add((x, y-1))
            
            #east
            if x < len(puzzle[y])-1 and puzzle[y][x+1] != "#":
                new_locations.add((x+1, y))

            #south
            if y < len(puzzle)-1 and puzzle[y+1][x] != "#":
                new_locations.add((x, y+1))

            #west
            if x > 0 and puzzle[y][x-1] != "#":
                new_locations.add((x-1, y))
        locations = new_locations

    result = len(locations)
    return result


def solve_part_2(puzzle):
    return "not solved yet"


if __name__ == "__main__":
    puzzle = read_puzzle("day21.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print (f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")

