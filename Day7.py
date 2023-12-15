import numpy as np
from collections import Counter

input_file = 'InputFiles/Day7.txt'

# turn input file into numpy array
data = open(input_file).read().split("\n")

# Score | [hand] | bet
array = np.array([[0] + [*row.split()[0]] + [row.split()[1]] for row in data])


def card_values(card):
    text_to_num = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
    if card in text_to_num:
        return text_to_num[card]
    else:
        return int(card)


def card_values_2(card):
    text_to_num = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}
    if card in text_to_num:
        return text_to_num[card]
    else:
        return int(card)


def hand_score(row):
    hand = row[1:6]
    frequency = Counter(hand)
    if len(frequency) == 1:  # Five of a kind
        return 6
    elif len(frequency) == 2:
        if frequency.most_common(1)[0][1] == 4:  # Four of a kind
            return 5
        else:  # Full House
            return 4
    elif len(frequency) == 3:
        if frequency.most_common(1)[0][1] == 3:  # Three of a kind
            return 3
        else:  # Three of a kind
            return 2
    elif len(frequency) == 4:  # One Pair
        return 1
    else:  # High card
        return 0


def hand_score_2(row):
    orig_hand = row[1:6]
    max_val = 0
    for option in ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]:
        option_val = 0
        if max_val == 6:
            break
        hand = [option if x == "J" else x for x in orig_hand]
        frequency = Counter(hand)
        if len(frequency) == 1:  # Five of a kind
            option_val = 6
        elif len(frequency) == 2:
            if frequency.most_common(1)[0][1] == 4:  # Four of a kind
                option_val = 5
            else:  # Full House
                option_val = 4
        elif len(frequency) == 3:
            if frequency.most_common(1)[0][1] == 3:  # Three of a kind
                option_val = 3
            else:  # Three of a kind
                option_val = 2
        elif len(frequency) == 4:  # One Pair
            option_val = 1
        else:  # High card
            option_val = 0

        if option_val > max_val:
            max_val = option_val
    return max_val


def part_1(array):
    for row_index in range(len(array)):
        row = array[row_index]
        array[row_index][0] = hand_score(row)
    # Convert card names to integer values
    vectorized_func = np.vectorize(card_values)
    game_array = vectorized_func(array)

    # Sort in losing to winning order
    sorted_arr = game_array[np.lexsort(np.transpose(game_array)[::-1])]

    # Get the final answer
    row_indices = np.arange(1, sorted_arr.shape[0] + 1)  # Get rankings
    score_column = sorted_arr[:, 6]
    products = score_column * row_indices
    print(sum(products))


def part_2(array):
    for row_index in range(len(array)):
        row = array[row_index]
        array[row_index][0] = hand_score_2(row)
    # Convert card names to integer values
    vectorized_func = np.vectorize(card_values_2)
    game_array = vectorized_func(array)

    # Sort in losing to winning order
    sorted_arr = game_array[np.lexsort(np.transpose(game_array)[::-1])]

    # Get the final answer
    row_indices = np.arange(1, sorted_arr.shape[0] + 1)  # Get rankings
    score_column = sorted_arr[:, 6]
    products = score_column * row_indices
    print(sum(products))


part_2(array)
