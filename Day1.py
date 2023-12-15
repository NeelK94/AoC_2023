import re

# Part 1
input_file = 'InputFiles/Day1.txt'

num_sum = 0


# Part 1
def get_num(text):
    numbers = re.findall(r'\d', text)
    return int(str(numbers[0]) + str(numbers[-1]))


with open(input_file, 'r') as file:
    for line in file:
        num_sum += get_num(line)

print(num_sum)



# Part 2


# Part 2
num_dict = {
    "zero" : "0",
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9",
    "0" : "0",
    "1" : "1",
    "2" : "2",
    "3" : "3",
    "4" : "4",
    "5" : "5",
    "6" : "6",
    "7" : "7",
    "8" : "8",
    "9" : "9"
}

num_dict_2 = {
    "0" : "0",
    "1" : "1",
    "2" : "2",
    "3" : "3",
    "4" : "4",
    "5" : "5",
    "6" : "6",
    "7" : "7",
    "8" : "8",
    "9" : "9"
}

def find_first_occurrence(text, substrings):
    occurrences = {}
    for substring in substrings:
        index = text.find(substring)
        occurrences[substring] = index

    filtered_occurrences = {k: v for k, v in occurrences.items() if v != -1}
    min_key = min(filtered_occurrences, key=filtered_occurrences.get)
    return num_dict[min_key]


def find_last_occurrence(text, substrings):
    occurrences = {}
    for substring in substrings:
        index = text.rfind(substring)
        occurrences[substring] = index

    filtered_occurrences = {k: v for k, v in occurrences.items() if v != -1}
    max_key = max(filtered_occurrences, key=filtered_occurrences.get)
    return num_dict[max_key]





# Part 2
num_sum_2 = 0

with open(input_file, 'r') as file:
    for line in file:
        num_sum_2 += int(find_first_occurrence(line, num_dict.keys()) + find_last_occurrence(line, num_dict.keys()))
print(num_sum_2)


# Part 1 alt
num_sum_3 = 0

with open(input_file, 'r') as file:
    for line in file:
        num_sum_3 += int(find_first_occurrence(line, num_dict_2.keys()) + find_last_occurrence(line, num_dict_2.keys()))
print(num_sum_3)

