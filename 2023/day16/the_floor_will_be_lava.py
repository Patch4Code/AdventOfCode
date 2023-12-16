# Advent of Code 2023
# Day 16: The Floor Will Be Lava
from time import perf_counter as pfc
from queue import Queue


def read_puzzle(filename):
    with open(filename) as datei:
        return datei.read().split("\n")


def solve_part_1(puzzle):   
    current_location, curret_direction = (0, 0), (1, 0) 
    return get_energized_amount(puzzle, current_location, curret_direction)


def solve_part_2(puzzle):
    
    staring_points_with_dir = []

    # add top starting points
    for i, element in enumerate(puzzle[0]):
        staring_points_with_dir.append(((i, 0), (0, 1)))
    # add bottom starting points
    for i, element in enumerate(puzzle[-1]):
        staring_points_with_dir.append(((i, len(puzzle)-1), (0, -1)))
    # add left starting points
    for i, row in enumerate(puzzle):
        staring_points_with_dir.append(((0, i), (1, 0)))
    # add right starting points
    for i, row in enumerate(puzzle):
        staring_points_with_dir.append(((len(puzzle[0])-1, i), (-1, 0)))
    
    energized_amounts = []

    # get energized_amounts for all starting points
    for element in staring_points_with_dir:
        current_location = element[0]
        curret_direction = element[1]
        current_energized_amount = get_energized_amount(puzzle, current_location, curret_direction)
        energized_amounts.append(current_energized_amount)
    
    # return the maximum energized_amount
    return max(energized_amounts)



def get_energized_amount(puzzle, current_location, curret_direction):

    my_queue = Queue()
    visited_states = set()
    my_queue.put((current_location, curret_direction)) 
    
    while not my_queue.empty():
        cur_loc, cur_dir = my_queue.get() 
        
        #already visited with same direction
        if (cur_loc, cur_dir) in visited_states:
            continue
        
        # . empty field
        elif puzzle[cur_loc[1]][cur_loc[0]] == ".":
            next_loc = (cur_loc[0] + cur_dir[0], cur_loc[1] + cur_dir[1])

            # Check if next_loc is within the bounds of the puzzle
            if 0 <= next_loc[0] < len(puzzle[0]) and 0 <= next_loc[1] < len(puzzle):
                my_queue.put((next_loc, cur_dir))

        # / mirror
        elif puzzle[cur_loc[1]][cur_loc[0]] == "/":
            changed_dir = (-cur_dir[1], -cur_dir[0])
            next_loc = (cur_loc[0] + changed_dir[0], cur_loc[1] + changed_dir[1])

            # Check if next_loc is within the bounds of the puzzle
            if 0 <= next_loc[0] < len(puzzle[0]) and 0 <= next_loc[1] < len(puzzle):
                my_queue.put((next_loc, changed_dir))

        # \ mirror
        elif puzzle[cur_loc[1]][cur_loc[0]] == "\\":
            changed_dir = (cur_dir[1], cur_dir[0])
            next_loc = (cur_loc[0] + changed_dir[0], cur_loc[1] + changed_dir[1])

            # Check if next_loc is within the bounds of the puzzle
            if 0 <= next_loc[0] < len(puzzle[0]) and 0 <= next_loc[1] < len(puzzle):
                my_queue.put((next_loc, changed_dir))

        # | splitter 
        elif puzzle[cur_loc[1]][cur_loc[0]] == "|":
            if cur_dir == (1, 0) or cur_dir == (-1, 0):
                changed_dir1, changed_dir2 = (0, 1), (0, -1)
                next_loc1, next_loc2 = (cur_loc[0] + changed_dir1[0], cur_loc[1] + changed_dir1[1]), (cur_loc[0] + changed_dir2[0], cur_loc[1] + changed_dir2[1])

                # Check if next_loc1 and next_loc2 are within the bounds of the puzzle
                if 0 <= next_loc1[0] < len(puzzle[0]) and 0 <= next_loc1[1] < len(puzzle):
                    my_queue.put((next_loc1, changed_dir1))
                if 0 <= next_loc2[0] < len(puzzle[0]) and 0 <= next_loc2[1] < len(puzzle):
                    my_queue.put((next_loc2, changed_dir2))
            else:
                next_loc = (cur_loc[0] + cur_dir[0], cur_loc[1] + cur_dir[1])

                # Check if next_loc is within the bounds of the puzzle
                if 0 <= next_loc[0] < len(puzzle[0]) and 0 <= next_loc[1] < len(puzzle):
                    my_queue.put((next_loc, cur_dir))

        # - splitter
        elif puzzle[cur_loc[1]][cur_loc[0]] == "-":    
            if cur_dir == (0, 1) or cur_dir == (0, -1):
                changed_dir1, changed_dir2 = (1, 0), (-1, 0)
                next_loc1, next_loc2 = (cur_loc[0] + changed_dir1[0], cur_loc[1] + changed_dir1[1]), (cur_loc[0] + changed_dir2[0], cur_loc[1] + changed_dir2[1])

                # Check if next_loc1 and next_loc2 are within the bounds of the puzzle
                if 0 <= next_loc1[0] < len(puzzle[0]) and 0 <= next_loc1[1] < len(puzzle):
                    my_queue.put((next_loc1, changed_dir1))
                if 0 <= next_loc2[0] < len(puzzle[0]) and 0 <= next_loc2[1] < len(puzzle):
                    my_queue.put((next_loc2, changed_dir2))
            else:
                next_loc = (cur_loc[0] + cur_dir[0], cur_loc[1] + cur_dir[1])

                # Check if next_loc is within the bounds of the puzzle
                if 0 <= next_loc[0] < len(puzzle[0]) and 0 <= next_loc[1] < len(puzzle):
                    my_queue.put((next_loc, cur_dir))

        # Mark the current state as visited by adding it to the set
        visited_states.add((cur_loc, cur_dir))

    # save energized elements and return the amount
    energized_set = set(element[0] for element in visited_states)
    return len(energized_set)


if __name__ == "__main__":
    puzzle = read_puzzle("day16.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print (f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")