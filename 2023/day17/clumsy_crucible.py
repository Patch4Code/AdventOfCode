# Advent of Code 2023
# Day 17: Clumsy Crucible
from time import perf_counter as pfc
from heapq import heappop, heappush


def read_puzzle(filename):
    with open(filename) as datei:
        return [list(map(int, row)) for row in datei.read().split("\n")]


def solve_part_1(puzzle):   
    
    return get_min_heatloss(puzzle, (0,0), (len(puzzle[0])-1, len(puzzle)-1))


def solve_part_2(puzzle):
    
    return get_min_heatloss(puzzle, (0,0), (len(puzzle)-1, len(puzzle[0])-1), 4, 10)


def get_min_heatloss(matrix, start_position, target_position, min_steps_before_turn = 0, max_steps = 3):
    rows = len(matrix)
    cols = len(matrix[0])

    pr_queue = []
    crucible_history = set()

    # (heatloss, position, x_dir, y_dir, steps)
    heappush(pr_queue, (0, start_position, 1, 0, 0))
    heappush(pr_queue, (0, start_position, 0, 1, 0))
    while pr_queue: 
        heatloss, position, x_dir, y_dir, steps = heappop(pr_queue)
        x, y = position

        if (position, x_dir, y_dir, steps) in crucible_history:
            continue

        if position == target_position and steps >= min_steps_before_turn:
            return heatloss
        
        crucible_history.add((position, x_dir, y_dir, steps))

        if steps >= min_steps_before_turn:
            if x_dir == 1 or x_dir == -1:
                if y+1 < rows:
                    heappush(pr_queue, (heatloss + matrix[y+1][x], (x, y+1), 0, 1, 1))
                if y-1 >= 0:
                    heappush(pr_queue, (heatloss + matrix[y-1][x], (x, y-1), 0, -1, 1))
    
            elif y_dir == 1 or y_dir == -1:
                if x+1 < cols:
                    heappush(pr_queue, (heatloss + matrix[y][x+1], (x+1, y), 1, 0, 1))
                if x-1 >= 0:
                    heappush(pr_queue, (heatloss + matrix[y][x-1], (x-1, y), -1, 0, 1))
            
        if steps < max_steps:
            if 0 <= x + x_dir < cols and 0 <= y + y_dir < rows:
                heappush(pr_queue, (heatloss + matrix[y + y_dir][x + x_dir], (x + x_dir, y + y_dir), x_dir, y_dir, steps+1))


if __name__ == "__main__":
    puzzle = read_puzzle("day17.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print (f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
