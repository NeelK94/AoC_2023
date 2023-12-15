import numpy as np
import pandas as pd
import math

input_file = 'InputFiles/Day8.txt'

# turn input file into numpy array
data = open(input_file).read().split("\n")

directions = [*data[0]]
n = len(directions)
codes = {}
for x in data[2:]:
    start = x.split(" = ")[0]
    L = x.split(" = ")[1][1:-1].split(", ")[0]
    R = x.split(" = ")[1][1:-1].split(", ")[1]
    codes[start] = {"L": L, "R": R}

'''
# PART 1
position = 'AAA'
count = 0

while True:
    count += 1
    dir = directions[(count-1) % n]

    position = codes[position][dir]

    if position == "ZZZ":
        break

print(count)

'''
# PART 2

# PART 2

pos_list = []
for k in codes.keys():
    if k[-1] == 'A':
        pos_list.append(k)

'''
count = 0
while True:
    count += 1
    fail_flag = 0
    dir = directions[(count - 1) % n]
    new_list = []
    for start in pos_list:
        position = codes[start][dir]
        if position[-1] != 'Z':
            fail_flag = 1
        new_list.append(position)
    pos_list = new_list.copy()

    if fail_flag == 0:
        break

print(count)
'''
cach = pd.DataFrame(columns = list(codes.keys()))

def get_final_characters(row):
    final_chars = set([str(x)[-1] for x in row])
    if len(final_chars) == 1:
        if final_chars.pop() == "Z":
            return True
    else:
        return False

def get_final_characters_2(row):
    final_chars = [str(x)[-1] for x in row]
    return final_chars.count("Z")

def check_win(df, start_cols):
    filt_df = df[start_cols]
    filt_df['Final_Chars'] = filt_df.apply(lambda row: get_final_characters(row), axis=1)
    win_row = filt_df.index[filt_df['Final_Chars'].idxmax()] if any(filt_df['Final_Chars']) else False
    return win_row

for k in codes.keys():
    new_col = []
    position = k
    for x in directions:
        position = codes[position][x]
        new_col.append(position)
    cach[k] = new_col

print(cach)

#cach['Final_Chars'] = cach.apply(lambda row: get_final_characters_2(row), axis=1)
#sorted_df = cach.sort_values(by='Final_Chars', ascending=False)
# Get columns that end in Z in row 262
print(cach.iloc[262].str.endswith('Z'))
columns_ending_with_Z = cach.columns[cach.iloc[262].str.endswith('Z')]
print(columns_ending_with_Z)

final_row_values_dict = {col: cach[col].iloc[-1] for col in cach.columns}
'''
for start in pos_list:
    print(f"\nSTART VALUE IS {start}")
    count = 0
    found_count = 0
    next_val = start
    while True:
        count += 1
        next_val = final_row_values_dict[next_val]
        if next_val in columns_ending_with_Z:
            print(f"FOUND Z AFTER {count - 1} COMPLETE CYCLES IN ROW 262")
            found_count += 1
        if found_count == 5:
            break
'''
# FDA has cycle length 73
# BPA has cycle length 43
# BVA has cycle length 67
# NDA has cycle length 79
# AAA has cycle length 61
# QCA has cycle length 59

# Find LCM of the above numbers and add 262:
lcm_result = math.lcm(73, 43, 67, 79, 61, 59)
print(lcm_result * (len(directions)) + 261)

print(len([1,2]))

# Try going row by row:
for start in pos_list:
    print(f"\nSTART VALUE IS {start}")
    count = 0
    next_val = start
    found_count = 0
    while True:
        count += 1
        dir = directions[(count - 1) % n]
        next_val = codes[next_val][dir]
        if next_val[-1] == 'Z':
            print(f"FOUND Z AFTER {count} ITERATIONS")
            found_count += 1
        if found_count == 5:
            break

lcm_result = math.lcm(19199, 11309, 17621, 20777, 16043, 15517)
print(lcm_result)

'''
count = 0
while True:
    count += 1
    for start in pos_list:
        position = start
        print(start)
        if cach[start].isnull().all():
            print('Adding to cach')
            new_col = []
            for x in directions:
                print(x)
                position = codes[position][x]
                print(position)
                new_col.append(position)
            cach[start] = new_col
    result = check_win(cach, pos_list)
    print("result")
    print(cach)
    print(result)
    if result is False:
        filt_df = cach[pos_list]
        pos_list = [x for x in filt_df.iloc[-1].tolist() if not pd.isna(x)]

        print(pos_list)
    else:
        ans = (count-1) * len(directions) + result + 1
        break
print(ans)
'''
'''
count = 0
while True:
    count += 1
    result = check_win(cach, pos_list)
    print("result")
    print(result)
    if result is False:
        filt_df = cach[pos_list]
        pos_list = [x for x in filt_df.iloc[-1].tolist() if not pd.isna(x)]
        print(pos_list)
    else:
        ans = (count-1) * len(directions) + result + 1
        break
print(ans)
'''