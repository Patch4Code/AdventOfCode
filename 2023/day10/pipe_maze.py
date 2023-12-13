# Advent of Code 2023
# Day 10: Pipe Maze

from time import perf_counter as pfc
from collections import deque

def read_puzzle(filename):
    with open(filename) as datei:
        return datei.read().split("\n")


def solve_part_1(puzzle):
    # Find start
    start_row, start_col = None, None
    for i, element in enumerate(puzzle):
        if 'S' in element:
            start_row = i
            start_col = element.index('S')
            break

    connected_pipes = find_adjacent_elements(puzzle, start_row, start_col)

    max_distance = max(cell for row in connected_pipes for cell in row)

    return max_distance


def solve_part_2(puzzle):
    return "no presentable solution"


def find_adjacent_elements(matrix, start_row, start_col):
    pipe_directions = {
        "|": ["n", "s"],
        "-": ["w", "e"],
        "L": ["n", "e"],
        "J": ["n", "w"],
        "7": ["s", "w"],
        "F": ["s", "e"],
        ".": [],
        "S": ["n", "s", "w", "e"]
    }

    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    distances = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    queue = deque([(start_row, start_col)])

    while queue:
        current_row, current_col = queue.popleft()
        visited[current_row][current_col] = True

        possible_directions = pipe_directions.get(matrix[current_row][current_col])

        for direction in possible_directions:
            # above
            if direction == "n" and current_row > 0 and "s" in pipe_directions.get(matrix[current_row-1][current_col]) and not visited[current_row-1][current_col]:
                queue.append((current_row-1, current_col))
                distances[current_row-1][current_col] = distances[current_row][current_col] + 1
            # below
            if direction == "s" and current_row < len(matrix)-1 and "n" in pipe_directions.get(matrix[current_row+1][current_col]) and not visited[current_row+1][current_col]:
                queue.append((current_row+1, current_col))
                distances[current_row+1][current_col] = distances[current_row][current_col] + 1
            # left
            if direction == "w" and current_col > 0 and "e" in pipe_directions.get(matrix[current_row][current_col-1]) and not visited[current_row][current_col-1]:
                queue.append((current_row, current_col-1))
                distances[current_row][current_col-1] = distances[current_row][current_col] + 1
            # right
            if direction == "e" and current_col < len(matrix[0])-1 and "w" in pipe_directions.get(matrix[current_row][current_col+1]) and not visited[current_row][current_col+1]:
                queue.append((current_row, current_col+1))
                distances[current_row][current_col+1] = distances[current_row][current_col] + 1

    return distances


if __name__ == "__main__":
    puzzle = read_puzzle("day10.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print (f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")

