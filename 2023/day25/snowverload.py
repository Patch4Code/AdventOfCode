# Advent of Code 2023
# Day 25: Snowverload
from time import perf_counter as pfc
import networkx as nx
import matplotlib.pyplot as plt

def read_puzzle(filename):
    with open(filename) as datei:
        return datei.read().split("\n")
    


def solve_part_1(puzzle):
    
    nodes = set()
    edges = set()
    for line in puzzle:
        component = line.split(":")[0]
        connections = line.split(":")[1].strip().split(" ")     
        nodes.add(component)
        for element in connections:
            nodes.add(element.strip())
            edges.add((component, element.strip()))
   
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", edge_color="gray", linewidths=1, alpha=0.7)
    plt.show()
    
    
    changed_edges = edges.copy()

    user_input = input("Type in the the 3 nodes in the middle --> a,b;c,d;e,f: ")
    for element in user_input.split(";"):
       node1 = element.split(",")[0]
       node2 = element.split(",")[1]
       changed_edges.discard((node1, node2))
       changed_edges.discard((node2, node1))
    
    newG = nx.Graph()
    newG.add_nodes_from(nodes)
    newG.add_edges_from(changed_edges)

    #extract the separated graphs
    resulting_graph_nodes = list(nx.connected_components(newG))
    result = len(resulting_graph_nodes[0])*len(resulting_graph_nodes[1])

    return result



def solve_part_2(puzzle):
    return "not all stars"



if __name__ == "__main__":
    puzzle = read_puzzle("day25.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print (f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")