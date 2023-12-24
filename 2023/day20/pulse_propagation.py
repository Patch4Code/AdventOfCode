# Advent of Code 2023
# Day 19: Pulse Propagation
from time import perf_counter as pfc
from collections import deque


def read_puzzle(filename):
    with open(filename) as datei:
        return datei.read().split("\n")
    


def solve_part_1(puzzle):
    
    #parsing
    module_config_dict = dict()
    conjunctions = set()
    for line in puzzle:
        name = line.split("-")[0].strip().replace("%", "").replace("&", "")
        type = line[0]
        destinations =  tuple((dest.strip()) for dest in line.split(">")[1].strip().split(","))

        if type == "%":
            module_config_dict[name] = [type, destinations, "off"]
        elif type == "&":
            conjunctions.add(name)
            module_config_dict[name] = [type, destinations, {}]
        else:
            module_config_dict[name] = [type, destinations]
 
    for name, content in module_config_dict.items():
        destinations = content[1]
        for dest in destinations:
            if dest  in conjunctions:
                module_config_dict[dest][2][name] = 0


    #logic  
    high_sent = 0
    low_sent = 0
    editable_module_config_dict = module_config_dict.copy() 

    for _ in range(1000):
        no_loop_found = True

        while no_loop_found:
            #button pressed
            queue = deque([("button", "broadcaster", 0)]) #deque(source, destination, state --> high=1, low=0)

            while queue:
                source, destination, state = queue.popleft()  

                if state == 0:
                    low_sent += 1
                elif state == 1:
                    high_sent += 1

                if destination not in editable_module_config_dict:
                    continue
                
                destination_content = editable_module_config_dict[destination]

                if destination_content[0] == "%":
                    if state == 0:
                        if destination_content[2] == "off":
                            for dest in destination_content[1]:
                                queue.append((destination, dest, 1))
                            editable_module_config_dict[destination][2] = "on"
                        else: #if destination_content[2] == "on"
                            for dest in destination_content[1]:
                                queue.append((destination, dest, 0))
                            editable_module_config_dict[destination][2] = "off"

                elif destination_content[0] == "&":
                    editable_module_config_dict[destination][2][source] = state
                    if all(value == 1 for value in editable_module_config_dict[destination][2].values()):
                        for dest in destination_content[1]:
                            queue.append((destination, dest, 0))
                    else:
                        for dest in destination_content[1]:
                            queue.append((destination, dest, 1))

                else: # broadcaster 
                    for dest in destination_content[1]:
                        queue.append((destination, dest, state))
            
            if editable_module_config_dict == module_config_dict:
                no_loop_found = False
            
    result = high_sent * low_sent
    return result


def solve_part_2(puzzle):
    return "not solved yet"


if __name__ == "__main__":
    puzzle = read_puzzle("day20.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print (f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")