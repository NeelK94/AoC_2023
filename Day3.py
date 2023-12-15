import pandas as pd
import numpy as np
import re

input_file = 'InputFiles/Day3.txt'

# turn input file into numpy array
txt_data = open(input_file).read().split()
data = []
for row in txt_data:
    data.append(list(row))

data = np.array(data)

# Add dots all around the array
dot_row = np.array(['.'] * data.shape[1])
data = np.vstack([dot_row, data, dot_row])

dot_col = np.array(['.'] * data.shape[0]).reshape(-1,1)
data = np.hstack([dot_col, data, dot_col])

digit_reg = re.compile(r'^[0-9]$')
special_char_reg = re.compile(r'[^0-9.]')


def check_surroundings(data, x, y):
    star_loc = False
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
               (0, 1), (1, -1), (1, 0), (1, 1)]
    for direction in directions:
        val = data[x + direction[0]][y + direction[1]]
        if special_char_reg.match(val):
            if val == '*':
                star_loc = (x + direction[0], y + direction[1])
            return star_loc, True
    return star_loc, False

def store_part_num(num_list):
    num_text = ''.join(num_list)
    return int(num_text)

gear_dict = {}
gear_ratio_sum = 0
star_location = False
store_num = []
part_num = False  # flag to determine if it is a part number or not
engine_sum = 0

for (row, col), val in np.ndenumerate(data):
    if val.isdigit():
        # add to store_num
        store_num.append(val)
        # call function to check surroundings and adjust flag
        if star_location is False:
            star_location = check_surroundings(data, row, col)[0]
        if part_num is False:
            part_num = check_surroundings(data, row, col)[1]
    else:
        # if part_num flag is up then call function to interpret digits and store
        if star_location is not False:
            if star_location in gear_dict:
                gear_dict[star_location].append(store_part_num(store_num))
            else:
                gear_dict[star_location] = [store_part_num(store_num)]
        # if part_num flag is up then call function to interpret digits and store
        if part_num is True:
            engine_sum += store_part_num(store_num)
        # reset everything
        part_num = False
        star_location = False
        store_num = []

print(engine_sum)
for location, gear_pair in gear_dict.items():
    if location is not False and len(gear_pair) == 2:
        gear_ratio_sum += gear_pair[0]*gear_pair[1]

print(gear_ratio_sum)