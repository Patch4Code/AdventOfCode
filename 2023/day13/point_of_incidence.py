# Advent of Code 2023
# Day 13: Point of Incidence

from time import perf_counter as pfc


def read_puzzle(filename):
    with open(filename) as datei:
        return [line.split("\n") for line in datei.read().split("\n\n")]


def solve_part_1(puzzle):
    
    summe = 0

    for block in puzzle:
        
        #find line of reflection vertically
        previous_line = ""
        possible_relectionline = -1
        for i, line in enumerate(block):
            if previous_line == "":
                previous_line = line
            elif line == previous_line:
                possible_relectionline = i
                if is_reflection_line_part1(block, possible_relectionline):
                    #print("Worked", block, possible_relectionline)
                    summe += (possible_relectionline)*100
                    
                    break
            previous_line = line        

        
        flipped_block = [list(row) for row in zip(*block)]
        previous_line = ""
        possible_relectionline = -1
        for i, line in enumerate(flipped_block):
            if previous_line == "":
                previous_line = line
            elif line == previous_line:
                possible_relectionline = i
                if is_reflection_line_part1(flipped_block, possible_relectionline):
                    #print("Worked", block, possible_relectionline)
                    summe += possible_relectionline
                    
                    break
            previous_line = line        
    
    return summe


def solve_part_2(puzzle):
    
    summe = 0

    for block in puzzle:
        
        #find smudge


        #find line of reflection vertically
        previous_line = ""
        for i, line in enumerate(block):
            if previous_line == "":
                previous_line = line
            else:
                if is_reflection_line_part2(block, i):
                    summe += (i)*100  
                    break      

        previous_line = ""
        flipped_block = [list(row) for row in zip(*block)]
        for i, line in enumerate(flipped_block):
                if previous_line == "":
                    previous_line = line
                else:
                    if is_reflection_line_part2(flipped_block, i):
                        summe += i
                        break  

    return summe


def is_reflection_line_part1(block, pos_relectline):
    above_part, below_part = block[:pos_relectline], block[pos_relectline:]
    #print("hello", above_part, below_part)
    
    for i, element in enumerate(above_part[::-1]):
        if i+1 > len(below_part):
            break
        if element != below_part[i]:
            return False 
    return True


def is_reflection_line_part2(block, pos_relectline):
    above_part, below_part = block[:pos_relectline], block[pos_relectline:] 
    differences = 0
    for i, element in enumerate(above_part[::-1]):
        if i+1 > len(below_part):
            break
        if element != below_part[i]:
            differences += number_of_differences(element, below_part[i])

    if differences == 1:
        return True
    else:
        return False


def number_of_differences(string1, string2):
    return sum(1 for a, b in zip(string1, string2) if a != b)


if __name__ == "__main__":
    puzzle = read_puzzle("day13.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print (f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")