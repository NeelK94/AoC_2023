import copy

import numpy as np
import threading
from copy import deepcopy
input_file = 'InputFiles/Day5.txt'

data_list = open(input_file).read()
section_headers = ['seeds', 'seed-to-soil map', 'soil-to-fertilizer map', 'fertilizer-to-water map',
            'water-to-light map', 'light-to-temperature map', 'temperature-to-humidity map',
            'humidity-to-location map']

map_dict = {}
# Populate map dictionary
for section_num in range(1, len(section_headers)):
    start = section_headers[section_num-1]
    end = section_headers[section_num]
    section = data_list[data_list.index(start) : data_list.index(end)]
    if section.split(":")[0] == 'seeds':
        map_dict[section.split(":")[0]] = section.split(":")[1].split()
    else:
        map_dict[section.split(":")[0]] = np.array(section.split(":")[1].split()).reshape(-1, 3)
else:
    section = data_list[data_list.index('humidity-to-location map'):]
    map_dict[section.split(":")[0]] = np.array(section.split(":")[1].split()).reshape(-1, 3)

seeds = map_dict['seeds']

def map_next(input, sec):
    map = map_dict[sec]
    for row in map:
        if int(row[1]) <= input < (int(row[1]) + int(row[2])):
            return (input - int(row[1])) + int(row[0])
    return int(input)

mapped_values = []
for seed in seeds:
    mapped_value = int(seed)
    for section in section_headers:
        if section == 'seeds':
            continue
        mapped_value = map_next(mapped_value, section)
    mapped_values.append(mapped_value)

print(min(mapped_values))


# PART 2
print("STARTING PART TWO")

seed_ranges = [(int(seeds[i]), int(seeds[i + 1]) if i + 1 < len(seeds) else None) for i in range(0, len(seeds), 2)]
#seed_ranges = [(1636419363, 2245243551)]
def map_next_range_2(input_ranges, sec):
    map = map_dict[sec]
    re_list = []
    for input in input_ranges:
        for row in map:
            diff = int(row[1]) - int(row[0])
            if int(row[1]) <= input[0] < (int(row[1]) + int(row[2])):

                split = int(row[2]) - input[0] + int(row[1])
                if split < input[1]:
                    re_list.append((input[0] - diff, split))
                    input = (input[0] + split, input[1] - split)

                else:
                    re_list.append((input[0] - diff, input[1]))
                    break
    return re_list


def map_next_range(input_ranges, sec):
    print(f"\nSection {sec}")
    #print(f"We have {len(input_ranges)} ranges to test")
    re_list = []  # new list of ranges to return for next section to evaluate
    for input in input_ranges:
        #print(f"new input \n")
        #map = map_dict[sec].copy()
        map = copy.deepcopy(map_dict[sec])
        while True:
            print(input)
            print(re_list)
            print("---")
            #print(f"Input: {input}")
            min_row_index = np.argmin(map[:, 1])
            row = map[min_row_index]
            #print(row)
            diff = int(row[1]) - int(row[0])
            if input[0] < int(row[1]):
                split = int(row[1]) - input[0]
                if split > input[1]:
                    re_list.append(input)
                    #print(f"APPENDING {input}")
                    break
                else:
                    re_list.append((input[0], split))
                    #print(f"APPENDING {(input[0], split - 1)}")
                    input = (input[0] + split, input[1] - split + 1)

            elif int(row[1]) <= input[0] < (int(row[1]) + int(row[2])):

                split = int(row[2]) + int(row[1]) - input[0]
                if split < input[1]:
                    re_list.append((input[0] - diff, split)) # PASSED!!!
                    #print(f"APPENDING {(input[0] - diff, split - 1)}")
                    input = (input[0] + split, input[1] - split)  # PASSED!!!

                else:
                    re_list.append((input[0] - diff, input[1]))  # PASSED!!!
                    #print(f"APPENDING {(input[0] - diff, input[1])}")
                    break
            else:
                if len(map) == 1: # PASSED!!!
                    re_list.append(input)
                    #print(f"APPENDING {input}")
                    break
                else:
                    map = np.delete(map, min_row_index, axis=0) # PASSED!!!

    print("FINAL")
    print(re_list)
    print([(x, x + y) for x, y in re_list])
    return re_list


range_list = seed_ranges
for section in section_headers:
    if section == 'seeds':
        continue
    range_list = map_next_range(range_list, section)

print('complete')
min_result = min(range_list, key=lambda x: x[0])
print(min_result)