# Advent of Code 2023
# Day 18: Lavaduct Lagoon
from time import perf_counter as pfc
from shapely.geometry import Polygon

def read_puzzle_part1(filename):
    with open(filename) as datei:
        return [(line.split()[0], int(line.split()[1])) for line in datei.read().split("\n")]
    
def read_puzzle_part2(filename):
    with open(filename) as datei:
        input = [line.split()[2].replace("(", "").replace(")", "") for line in datei.read().split("\n")]
        direction_values = {0: "R", 1: "D", 2: "L", 3: "U"}
        new_input = []
        for line in input:
            new_dir = int(line[-1], 16)
            new_len = int(line[1:-1], 16)
            new_input.append((direction_values[new_dir], new_len))   
        return new_input



def solve(puzzle):   
    
    dirs = {"R": (1, 0), "D": (0, 1), "L": (-1, 0), "U": (0, -1)}

    x, y = 0, 0
    points = [(x, y)]
    for line in puzzle:
        dir_x, dir_y = dirs[line[0]] 
        len= line[1]
        x += dir_x * len
        y += dir_y * len
        points.append((x, y))
      
    polygon = Polygon(points)
    area_inside_polygon = polygon.area
    area_outside_polygon = sum(line[1] for line in puzzle) / 2 + 1
    total_area = area_inside_polygon + area_outside_polygon
    
    return total_area



if __name__ == "__main__":
    puzzle1 = read_puzzle_part1("day18.txt")
    puzzle2 = read_puzzle_part2("day18.txt")
    start = pfc()
    result1 = solve(puzzle1)
    print (f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve(puzzle2)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")