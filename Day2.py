import re

input_file = 'InputFiles/Day2.txt'
#'''
games = open(input_file).read().split("\n")
print(games)
game_map = {}

for game in games:
    game_num = game.split(": ")[0][4:].strip()
    sub_dicts = []
    for selection in game.split(": ")[1].split("; "):
        sub_dict = {}
        colours = selection.split(", ")
        for colour in colours:
            sub_dict[colour.split(" ")[1]] = colour.split(" ")[0]
        sub_dicts.append(sub_dict)
    game_map[game_num] = sub_dicts
    #game_map[game_num] = game.split(": ")[1].split("; ")

print(game_map.keys())
ID_sum = 0
for game_num, selections in game_map.items():
    print(f"\nChecking game {game_num}")
    fail_flag = 0
    for selection in selections:
        blues = 0
        reds = 0
        greens = 0
        if 'blue' in selection.keys():
            blues += int(selection['blue'])
        if 'green' in selection.keys():
            greens += int(selection['green'])
        if 'red' in selection.keys():
            reds += int(selection['red'])
        if blues > 14 or greens > 13 or reds > 12:
            fail_flag = 1
            break
    if fail_flag == 0:
        ID_sum += int(game_num)

print(ID_sum)
#'''
# Part 2

total_power = 0
for game_num, selections in game_map.items():
    blue_cubes = 0
    red_cubes = 0
    green_cubes = 0
    for selection in selections:
        blues = 0
        reds = 0
        greens = 0
        if 'blue' in selection.keys():
            blues += int(selection['blue'])
        if 'green' in selection.keys():
            greens += int(selection['green'])
        if 'red' in selection.keys():
            reds += int(selection['red'])
        if blues > blue_cubes:
            blue_cubes = blues
        if greens > green_cubes:
            green_cubes = greens
        if reds > red_cubes:
            red_cubes = reds
    total_power += blue_cubes * green_cubes * red_cubes

print(total_power)
