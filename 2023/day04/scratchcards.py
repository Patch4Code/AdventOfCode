# Advent of Code 2023
# Day 4: Scratchcards 

from time import perf_counter as pfc

def read_puzzle(filename):
    with open(filename) as datei:
        return datei.read().split('\n')
    

"""
Part 1:
Help an Elf determine the total points for a pile of scratchcards on a new island. 
Each scratchcard contains winning numbers and your numbers, with points awarded for matches. 
The first match earns one point, and subsequent matches double the points. 
Determine the total points for the pile of scratchcards by adding up all the points for each card.
"""
def solve_part_1(puzzle):

    result = 0

    for line in puzzle:
        found_matches = 0
        
        # Split the line to two separate lsits winning numbers and your numbers.
        # -> map() applies str.split() to each element of the resulting lists 
        # -> str.split() returns a list of strings
        winning_nums, my_nums = map(str.split, line.split(":")[1].split("|"))  
                                                                                 
        # Check for matches and calculate points.
        for num in my_nums:
            if num in winning_nums and found_matches == 0:
                found_matches += 1
            elif num in winning_nums:
                found_matches *= 2
        
        # Add the calculated points to the total result.
        result += found_matches
    
    return result


"""
Determine the total number of scratchcards you end up with by processing original 
and copied scratchcards until no more cards are won. Wins are based on the number 
of matching numbers, generating copies equal to the matches, creating a cascading effect.
"""
def solve_part_2(puzzle):
    
    # Initialize a list to keep track of the number of copies for each scratchcard.
    list_of_cards = [1] * len(puzzle)

    # Loop through each scratchcard in the puzzle input.
    for card_nr, line in enumerate(puzzle):
        
        #  Split the line to two separate lists winning numbers and your numbers.
        winning_nums, my_nums = map(str.split, line.split(":")[1].split("|"))

        # Count the number of matches for the current scratchcard.
        found_matches = sum((num in winning_nums) for num in my_nums)*1

        # If there are matches, update the list_of_cards to simulate winning copies.
        if found_matches > 0:
                # Loop over the cards after the current card -> range depending on found_matches
                for i in range(card_nr + 1 , card_nr + found_matches + 1):
                    if i <= len(puzzle):
                        list_of_cards[i] += list_of_cards[card_nr]  
            
    return sum(list_of_cards) 



if __name__ == "__main__":
    puzzle = read_puzzle("day04.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print (f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
