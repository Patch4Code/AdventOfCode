# Advent of Code 2023
# Day 19: Aplenty 
from time import perf_counter as pfc


def read_puzzle(filename):
    with open(filename) as datei:
        input = datei.read().split("\n\n")
        workflows = input[0].split("\n")
        parts = input[1].split("\n")
        return workflows, parts
    


def solve_part_1(puzzle):
    
    workflows = {}
    parts = []
    
    #build parts list
    for part_parameter in puzzle[1]:   
            part_parameters = part_parameter.replace("{", "").replace("}", "").split(",")
            part_dict = dict((parameter.split("=")[0], int(parameter.split("=")[1])) for parameter in part_parameters)
            parts.append(part_dict)

    #build workflow dict
    for workflow in puzzle[0]:
        workflow_procedure = []
        for element in  workflow.split("{")[1].replace("}", "").split(","):
            if "<" in element or ">" in element:
                 char = element[0]
                 condition = element.split(":")[0][1:] 
                 destination = element.split(":")[1]
                 workflow_procedure.append((char, condition, destination))
            else:
                 workflow_procedure.append((1, "==1", element))

        workflows[workflow.split("{")[0]] = workflow_procedure
      
    #Task
    result = 0
    for part in parts:
        if(get_workflow_result(part, workflows, "in")) == "A":
             result += sum(part.values())
               
    return result



def solve_part_2(puzzle):
    return "not solved yet"



def get_workflow_result(part, workflows, workflow_name):
    
    if workflow_name == "A":
         return "A"
    if workflow_name == "R":
         return "R"
        
    workflow = workflows[workflow_name] 
    for i, element in enumerate(workflow):

        if workflow[-1] == element:
             return get_workflow_result(part, workflows, element[2])
         
        if eval(f"{part[element[0]]} {element[1]}"):
            return get_workflow_result(part, workflows, element[2])



if __name__ == "__main__":
    puzzle = read_puzzle("day19.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print (f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")

