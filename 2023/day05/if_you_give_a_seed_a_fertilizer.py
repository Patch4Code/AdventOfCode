# Advent of Code 2023
# Day 5: If You Give A Seed A Fertilizer

from time import perf_counter as pfc


def read_puzzle(filename):
    with open(filename) as datei:
        return datei.read().split('\n')


def solve_part_1(puzzle):
    #Data
    seed_to_spoil = read_and_process_file("day05_sts.txt")
    soil_to_fertilizer = read_and_process_file("day05_stf.txt")
    fertilizer_to_water = read_and_process_file("day05_ftw.txt")
    water_to_light = read_and_process_file("day05_wtl.txt")
    light_to_temperature = read_and_process_file("day05_lts.txt")
    temperature_to_humidity = read_and_process_file("day05_tth.txt")
    humidity_to_location = read_and_process_file("day05_htl.txt")

    seeds = [int(seed) for seed in puzzle[0].split(":")[1].strip().split()]

    location_list = []	
    for seed in seeds:
        #seed-to-soil map
        soil_value = convert_to_next_type(seed_to_spoil, seed)
    
        #soil-to-fertilizer map
        fertilizer_value = convert_to_next_type(soil_to_fertilizer, soil_value)
    
        #fertilizer-to-water map
        water_value = convert_to_next_type(fertilizer_to_water, fertilizer_value)
        #print("water_value", water_value)

        #water-to-light map
        light_value = convert_to_next_type(water_to_light, water_value)


        #light-to-temperature map
        temp_value = convert_to_next_type(light_to_temperature, light_value)


        #temperature-to-humidity map
        humidity_value = convert_to_next_type(temperature_to_humidity, temp_value)


        #humidity-to-location map
        location_value = convert_to_next_type(humidity_to_location, humidity_value)
        location_list.append(location_value)

    lowest_location = min(location_list)
    return lowest_location


def solve_part_2(puzzle):
    return "Not properly solved"


def read_and_process_file(file_path):
    data_list = []

    with open(file_path, 'r') as file:
        for line in file:
            # Splitte die Zeile an Leerzeichen und konvertiere die Werte zu integers
            values = [int(x) for x in line.strip().split()]
            
            # Überprüfe, ob die Zeile genau drei Werte enthält
            if len(values) == 3:
                data_list.append(values)

    return data_list

def convert_to_next_type(map, value_to_convert):
    
    converted_value = -1
    for line in map:
        
        #print("line 0, 1, 2: ", line[0], line[1], line[2])
        if value_to_convert in range(line[1], line[1]+line[2]):
            #print("true")
            converted_value = line[0] + (value_to_convert - line[1])
            break
    if converted_value == -1:
        converted_value = value_to_convert

    return converted_value

if __name__ == "__main__":
    puzzle = read_puzzle("day05.txt")
    start = pfc()
    result1 = solve_part_1(puzzle)
    print (f"Teil 1: {result1} ({pfc()-start:.4f}s)")
    start = pfc()
    result2 = solve_part_2(puzzle)
    print(f"Teil 2: {result2} ({pfc() - start:.4f}s)")
