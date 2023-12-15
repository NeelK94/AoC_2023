from itertools import combinations
import re
from functools import lru_cache

input_file = 'InputFiles/Day12.txt'
data_list = open(input_file).read().split("\n")
data_split = [["." + x.split(" ")[0] + ".", x.split(" ")[1]] for x in data_list]
data_split_unfolded = [["." + x.split(" ")[0] + "?" + x.split(" ")[0] + "?" + x.split(" ")[0] + "?" + x.split(" ")[0] +
                        "?" + x.split(" ")[0] + ".", x.split(" ")[1] + "," + x.split(" ")[1] + "," + x.split(" ")[1] +
                        "," + x.split(" ")[1] + "," + x.split(" ")[1]] for x in data_list]


def build_regex(nums):
    num_list = [int(num) for num in nums.split(",")]
    rgx = "\\.+"
    for num in num_list:
        rgx += "#{" + str(num) + "}\\.+"
    return rgx


def get_options(row, nums):
    hash_count = sum([int(num) for num in nums.split(",")]) - row.count('#')
    poss_locations = [index for index, char in enumerate(row) if char == '?']
    all_options = []
    all_combinations = list(combinations(poss_locations, hash_count))
    for combi in all_combinations:
        blank_row = list(row.replace("?", "."))
        for location in combi:
            blank_row[location] = "#"
        all_options.append(''.join(blank_row))
    return all_options


@lru_cache
def get_options_2(row, nums):
    print(row)
    if not row:
        if not nums:
            return 1  # Successfully allocated all nums
        else:
            return 0

    if not nums:
        if any("#" in x for x in row):
            return 0
        else:
            return 1
    if row[0] == "":
        return get_options_2(row[1:], nums)
    if len(row[0]) < nums[0]:  # Ignore group if not enough space for first num
        if "#" in row[0]:
            return 0
        else:
            return get_options_2(row[1:], nums)

    elif row[0][0] == "#":
        if len(row[0]) == nums[0]:  # Add all hashtags and consider next group
            return get_options_2(row[1:], nums[1:])
        if row[0][nums[0]] == "#":  # Dead end
            return 0
        hash_count = 0  # count consecutive hashes
        for x in row[0]:
            if x == "#":
                hash_count += 1
            else:
                break
        if hash_count <= nums[0]:
            new_row = list(row)
            new_row[0] = new_row[0][nums[0] + 1:]
            return get_options_2(tuple(new_row), nums[1:])
        new_row = list(row)
        new_row[0] = new_row[0][nums[0] + 1:]
        return get_options_2(tuple(new_row), nums[1:])

    elif row[0][0] == "?":
        dmg = list(row)
        dmg[0] = "#" + dmg[0][1:]
        fix = list(row)
        fix[0] = fix[0][1:]
        dmg = tuple(dmg)
        fix = tuple(fix)
        return get_options_2(dmg, nums) + get_options_2(fix, nums)



count = 0
for line in range(len(data_list)):
    row = data_split_unfolded[line][0]
    nums = data_split_unfolded[line][1]
    group_springs = tuple([x for x in row.split(".") if x != ""])
    num_list = tuple([int(num) for num in nums.split(",")])
    count += get_options_2(group_springs, num_list)


print(count)


'''
total_combinations = 0
for row in data_split_unfolded:
    print(row)
    success = 0
    r, nums = row
    rgx = build_regex(nums)
    options = get_options(r, nums)
    for option in options:
        matches = re.search(rgx, option)
        if matches:
            success += 1
    total_combinations += success
    print(success)

print(total_combinations)
'''