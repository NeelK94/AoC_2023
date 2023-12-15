import pandas as pd

input_file = 'InputFiles/Day4.txt'


def get_score(num):
    if num > 0:
        score = 1 * 2 ** (num - 1)
    else:
        score = 0
    return score


def part_one():
    total_score = 0
    with open(input_file, 'r') as file:
        for line in file:
            split_list = line.split(": ")[1].replace("  ", " ").strip().split(" | ")
            target_nums = set(split_list[0].split(" "))  # Winning numbers
            my_nums = set(split_list[1].split(" "))  # Numbers on the ticket

            matches = len(target_nums & my_nums)
            total_score += get_score(matches)

    print(total_score)


def part_two():
    # count is the number of cards you have yet to use, aggregate is a sum of all received cards.
    card_df = pd.DataFrame(columns=['card_num', 'score', 'count', 'aggregate'])

    # Initiate dataframe
    with open(input_file, 'r') as file:
        for line in file:
            card_number = line[5:].split(": ")[0].strip()
            card_vals = line[5:].split(": ")[1]
            split_list = card_vals.replace("  ", " ").strip().split(" | ")
            target_nums = set(split_list[0].split(" "))  # Winning numbers
            my_nums = set(split_list[1].split(" "))  # Numbers on the ticket

            matches = len(target_nums & my_nums)
            card_df.loc[len(card_df)] = [card_number, matches, 1, 1]


    # Run simulation
    for index in range(len(card_df)):
        row = card_df.iloc[index]
        if row['score'] > 0:
            for copy in range(1, row['score'] + 1):
                card_df.loc[index + copy, 'count'] += row['count']
                card_df.loc[index + copy, 'aggregate'] += row['count']
        card_df.loc[index, 'count'] = 0

    print(card_df['aggregate'].sum())


if __name__ == "__main__":
    part_one()
    part_two()