# Advent of Code 2023
# Day 19: Never Tell Me The Odds
from time import perf_counter as pfc


def read_puzzle(filename):
    with open(filename) as datei:
        return datei.read().split("\n")
    


def solve_part_1(puzzle):
    
    coords = [[(int(line.split(",")[0].strip()), (int(line.split(",")[1].strip()))), (int(line.split("@")[1].split(",")[0].strip()), int(line.split("@")[1].split(",")[1].strip()))] for line in puzzle]
    
    lines = []
    for coord in coords:
        start = coord[0]
        end = (start[0]+coord[1][0], start[1]+coord[1][1])
        lines.append([start, end])

    combinations = []
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            combinations.append((lines[i], lines[j]))
    
    result = 0
    for combination in combinations:
        x1, y1 = combination[0][0]
        x2, y2 = combination[0][1]
        x3, y3 = combination[1][0]
        x4, y4 = combination[1][1]

        schnitt = line_intersection((combination[0][0], combination[0][1]),(combination[1][0], combination[1][1]))
        direction1 = (x2 - x1, y2 - y1)
        direction2 = (x4 - x3, y4 - y3)

        at_least = 200000000000000
        at_most = 400000000000000

        schnitt_x = schnitt[0]
        schnitt_y = schnitt[1]
        if (at_least <= schnitt_x <= at_most and at_least <= schnitt_y <= at_most):                 
                if((schnitt_x-x1)* direction1[0] >= 0 and 
                   (schnitt_y-y1)* direction1[1] >= 0 and 
                   (schnitt_x-x3)* direction2[0] >= 0 and 
                   (schnitt_y-y3)* direction2[1] >= 0):
                    
                    result += 1

    return result



def solve_part_2(puzzle):
    return "not solved yet"



def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return (-1, -1)

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y



if __name__ == "__main__":
    puzzle = read_puzzle("day24.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print (f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")