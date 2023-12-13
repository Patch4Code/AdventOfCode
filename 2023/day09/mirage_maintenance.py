# Advent of Code 2023
# Day 9: Mirage Maintenance

from time import perf_counter as pfc

def read_puzzle(filename):
    with open(filename) as datei:
        return datei.read().split("\n")


def solve(puzzle):
    
    summe1 = 0
    summe2 = 0
    for line in puzzle:
        #get explorated values
        values = [int(v) for v in line.split()]
        history_list = []
        history_list.append(values)

        while(any(values)):
            list = []
            for i, value in enumerate(values):
                #add values next to each other and make new list from them
                if (i+1 < len(values)):
                    list.append(values[i+1] - values[i])
            values = list
            history_list.append(values)

        zwischen_summe = 0
        for element in history_list:
            zwischen_summe += element[-1]
        summe1+=zwischen_summe

        zwischen_summe2 = 0
        for element in reversed(history_list):
            zwischen_summe2 = element[0]-zwischen_summe2
        summe2+=zwischen_summe2
    
    return summe1, summe2



if __name__ == "__main__":
    puzzle = read_puzzle("day09.txt")
    start = pfc()
    result1, result2 = solve(puzzle)
    print (f"Teil 1: {result1}\nTeil 2: {result2}\n({pfc()-start:.4f}s)")


