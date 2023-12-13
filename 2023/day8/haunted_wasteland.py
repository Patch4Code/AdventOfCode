# Advent of Code 2023
# Day 8: Haunted Wasteland

from time import perf_counter as pfc
import math

def read_puzzle(filename):
    with open(filename) as datei:
        return datei.read().split("\n\n")


def solve_part_1(puzzle):
    
    navigation_instructions = puzzle[0]
    string = puzzle[1].split("\n")
    network_of_nodes = [(line.split("=")[0].strip(), line.split("=")[1].split(",")[0].replace("(", "").strip(), line.split("=")[1].split(",")[1].replace(")", "").strip()) for line in string]
    #[('AAA', 'BBB', 'CCC'), ('BBB', 'DDD', 'EEE'), ('CCC', 'ZZZ', 'GGG'), ('DDD', 'DDD', 'DDD'), ('EEE', 'EEE', 'EEE'), ('GGG', 'GGG', 'GGG'), ('ZZZ', 'ZZZ', 'ZZZ')]

    next_node = "AAA"
    step_counter = 0

    while True:
        for instruction in navigation_instructions:
            currrent_node = find_and_get_current_node(network_of_nodes, next_node)
            if instruction == "R":
                next_node = currrent_node[2]
                step_counter += 1

            elif instruction == "L":
                next_node = currrent_node[1]
                step_counter += 1

            if next_node == "ZZZ": break
        
        if next_node == "ZZZ": break

    return step_counter


def solve_part_2(puzzle):
    
    navigation_instructions = puzzle[0]
    string = puzzle[1].split("\n")
    network_of_nodes = [(line.split("=")[0].strip(), line.split("=")[1].split(",")[0].replace("(", "").strip(), line.split("=")[1].split(",")[1].replace(")", "").strip()) for line in string]
    #[('AAA', 'BBB', 'CCC'), ('BBB', 'DDD', 'EEE'), ('CCC', 'ZZZ', 'GGG'), ('DDD', 'DDD', 'DDD'), ('EEE', 'EEE', 'EEE'), ('GGG', 'GGG', 'GGG'), ('ZZZ', 'ZZZ', 'ZZZ')]

    nodes_starting_list = [node[0] for node in network_of_nodes if node[0][2] == "A"]
    
    step_set = set()
    for start_node in nodes_starting_list:
        current_node = start_node
        step_counter = 0

        while True:
            if current_node.endswith("Z"): 
                step_set.add(step_counter)
                break

            for instruction in navigation_instructions:
                step_counter += 1
                if instruction == "R":
                    current_node = find_and_get_current_node(network_of_nodes, current_node)[2] 
                elif instruction == "L":
                    current_node = find_and_get_current_node(network_of_nodes, current_node)[1]

    result = math.lcm(*step_set)
    return result


def find_and_get_current_node(network_of_nodes, next_node):
    for node in network_of_nodes:
        if node[0] == next_node:
            return node
        

if __name__ == "__main__":
    puzzle = read_puzzle("day08.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print (f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")

