# Advent of Code 2023
# Day 15: Lens Library
from time import perf_counter as pfc

def read_puzzle(filename):
    with open(filename) as datei:
        return [element.strip() for element in datei.read().split(",")]


def solve_part_1(puzzle):   
    return sum (hash_algorithm(string) for string in puzzle)


def solve_part_2(puzzle):
    boxes = [{} for _ in range(256)]
    
    for string in puzzle:        
        if "=" in string:    
            label = string.split("=")[0].strip()
            value = int(string.split("=")[1].strip())
            box_nr = hash_algorithm(label)
            
            boxes[box_nr][label] = value              
        
        else: # if "-" string  
            label = string.split("-")[0].strip()
            box_nr = hash_algorithm(label)
            
            if label in boxes[box_nr]:
                del boxes[box_nr][label]      
    
    return sum(box_nr * slot_nr * value for box_nr, box in enumerate(boxes, start=1) for slot_nr, (_, value) in enumerate(box.items(), start=1))


def hash_algorithm(string):
    cur_val = 0
    for char in string:
        ascii_code = ord(char) 
        cur_val = ((cur_val + ascii_code)*17)%256
    return cur_val


if __name__ == "__main__":
    puzzle = read_puzzle("day15.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print (f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")