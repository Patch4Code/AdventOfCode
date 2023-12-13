# Advent of Code
# Day 1: Trebuchet?!

from time import perf_counter as pfc


def read_puzzle(filename):
    with open(filename) as datei:
        return datei.read().split('\n')
    


def solve_part_1(puzzle):
    
    total_sum = 0
    for line in puzzle:
        nums = ""
        for char in line:
            if char.isdigit():
                nums += char
        total_sum += int(nums[0] + nums[len(nums)-1])
    
    return total_sum


#Hinweis --> eightwo --> 82
def solve_part_2(puzzle):
    num_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    
    total_sum = 0

    for line in puzzle:
        nums = "" # Variable to store numbers found in the current line
        curr_str = ""

        for char in line:
            curr_str += char # Adding the current character to the current string to remember 

            # Checking if the current character is a digit
            if char.isdigit():
                nums += char
                curr_str = "" #reset current string

            # Checking if any element of the dictionary is in the current string
            elif any(word in curr_str for word in num_dict): 
                found_word = next(word for word in num_dict if word in curr_str) # find the word from the dict in the current string
                nums += num_dict[found_word]
                curr_str = curr_str[len(curr_str) - len(found_word):] # cut down current string
            
        total_sum += int(nums[0] + nums[-1])

    return total_sum


if __name__ == "__main__":
    puzzle = read_puzzle("day1.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print (f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")

