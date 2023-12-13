# Advent of Code 2023
# Day 7: Camel Cards

from time import perf_counter as pfc
from collections import Counter

def read_puzzle(filename):
    with open(filename) as datei:
        return datei.read().split('\n')


def solve_part_1(puzzle):
    
    def sort_by_cardranks_function(string):
        result = []

        for char in string:
            if(char == " "):
                break
            if char in same_rank:
                result.append(same_rank[char])
            else:
                result.append(card_ranks[char])
        return result

    result = 0
    
    card_ranks = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
    ordered_hands_map = {}

    for line in puzzle:
        hand_string = line.split()[0]
        ordered_hands_map[line] = check_hand(hand_string)
        ordered_hands_map = dict(sorted(ordered_hands_map.items()))

    for value in range(1, 8):
        same_rank = [k for k, v in ordered_hands_map.items() if v == value]
        if len(same_rank) > 1:
            same_rank_sorted = sorted(same_rank, key= sort_by_cardranks_function, reverse=True)
            for index, card_string in enumerate(same_rank_sorted):
                ordered_hands_map[card_string] += index/len(same_rank_sorted)
            
    ordered_hands_map = dict(sorted(ordered_hands_map.items(),key=lambda item: item[1], reverse=True))

    for i, string in enumerate(ordered_hands_map, start=1):
        result += (i * int(string.split()[1]))
            
    return result


def solve_part_2(puzzle):
    def sort_by_cardranks_function(string):
        result = []
        for char in string:
            if(char == " "):
                break
            if char in same_rank:
                result.append(same_rank[char])
            else:
                result.append(card_ranks[char])
        return result
    
    result = 0
    
    card_ranks = {"A": 14, "K": 13, "Q": 12, "T": 11, "9": 10, "8": 9, "7": 8, "6": 7, "5": 6, "4": 5, "3": 4, "2": 3, "J": 2}
    ordered_hands_map = {}

    for line in puzzle:
        hand_string = line.split()[0]
        ordered_hands_map[line] = check_hand_part2(hand_string)
        ordered_hands_map = dict(sorted(ordered_hands_map.items()))

    for value in range(1, 8):
        same_rank = [k for k, v in ordered_hands_map.items() if v == value]
        if len(same_rank) > 1:
            same_rank_sorted = sorted(same_rank, key= sort_by_cardranks_function, reverse=True)
            for index, card_string in enumerate(same_rank_sorted):
                ordered_hands_map[card_string] += index/len(same_rank_sorted)
            
    ordered_hands_map = dict(sorted(ordered_hands_map.items(),key=lambda item: item[1], reverse=True))

    for i, string in enumerate(ordered_hands_map, start=1):
        result += (i * int(string.split()[1]))
    
    return result


def check_hand(hand):
    counts = Counter(hand)

    if 5 in counts.values():
        return 1.0 #"Five of a kind"
    elif 4 in counts.values():
        return 2.0 #"Four of a kind"
    elif 3 in counts.values() and 2 in counts.values():
        return 3.0 #"Full House"
    elif 3 in counts.values():
        return 4.0 #"Three of a kind"
    elif list(counts.values()).count(2) == 2:
        return 5.0 #"Two pair"
    elif 2 in counts.values():
        return 6.0 #"One pair"
    else:
        return 7.0 #"High Card"


def check_hand_part2(hand):
    j_count = 0
    for char in hand:
        if char == "J":
            j_count += 1

    hand = hand.replace("J", "")
    counts = Counter(hand)
    #5 joker
    if j_count == 5:
        return 1.0 #"Five of a kind"
    #4 joker
    elif j_count == 4:
        return 1.0 #"Five of a kind"
    #3 joker
    elif j_count == 3:
        if 2 in counts.values(): #ein paar?
            return 1.0
        else:
            return 2.0 #"Four of a kind"
    #2 joker
    elif j_count == 2:
        if 3 in counts.values(): # drei gleiche?
            return 1.0 
        elif 2 in counts.values():#ein paar?
            return 2.0
        else:                     #kein paar
            return 4.0
    #1 joker
    elif j_count == 1:
        if 4 in counts.values():
            return 1.0
        elif 3 in counts.values():
            return 2.0
        elif list(counts.values()).count(2) == 2:
            return 3.0
        elif 2 in counts.values():
            return 4.0
        else:
            return 6.0
    #0 joker
    else: 
        if 5 in counts.values():
            return 1.0 #"Five of a kind"
        elif 4 in counts.values():
            return 2.0 #"Four of a kind"
        elif 3 in counts.values() and 2 in counts.values():
            return 3.0 #"Full House"
        elif 3 in counts.values():
            return 4.0 #"Three of a kind"
        elif list(counts.values()).count(2) == 2:
            return 5.0 #"Two pair"
        elif 2 in counts.values():
            return 6.0 #"One pair"
        else:
            return 7.0 #"High Card"


if __name__ == "__main__":
    puzzle = read_puzzle("day07.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print (f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
