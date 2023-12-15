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


# PART 2

# PART 2

pos_list = []
for k in codes.keys():
    if k[-1] == 'A':
        pos_list.append(k)
count = 0
while True:
    count += 1
    fail_flag = 0
    dir = directions[(count - 1) % n]
    new_list = []
    print(pos_list)
    for start in pos_list:
        position = codes[start][dir]
        if position[-1] != 'Z':
            fail_flag = 1
        new_list.append(position)
    pos_list = new_list.copy()

    if fail_flag == 0:
        break

print(count)