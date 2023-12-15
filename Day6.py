import numpy as np
import math

input_file = 'InputFiles/Day6.txt'

# turn input file into numpy array
txt_data = open(input_file).read().split("\n")

times = txt_data[0].split(":")[1].split()
time_joined = ''.join(times)

distances = txt_data[1].split(":")[1].split()
dist_joined = ''.join(distances)

array = np.array([times, distances]).astype(int)
array_joined = np.array([time_joined, dist_joined])


def find_roots(a, b, c):
    dis_form = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis_form))
    root_1 = (-b + sqrt_val) / (2 * a)
    root_2 = (-b - sqrt_val) / (2 * a)
    return [root_1, root_2]


def num_wins(vals):
    t, d = vals
    [t1, t2] = find_roots(-1, t, (-d-1))

    min_time = math.ceil(t1)
    max_time = math.floor(t2)

    return max_time - min_time + 1


# Part 1
ans = np.prod(np.apply_along_axis(num_wins, 1, array.transpose()))
print(ans)


# Part 2
x = num_wins([int(array_joined[0]), int(array_joined[1])])
print(x)


