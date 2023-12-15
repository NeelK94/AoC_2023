import numpy as np
input_file = 'InputFiles/Day11.txt'
data_list = open(input_file).read().split("\n")
universe = np.array([list(x) for x in data_list])

empty_rows = []
empty_cols = []
for row_index in range(len(universe)):
    row = universe[row_index]
    if set(row) == {"."}:
        empty_rows.append(row_index)
for row_index in range(len(universe.transpose())):
    row = universe.transpose()[row_index]
    if set(row) == {"."}:
        empty_cols.append(row_index)


def find_galaxies(np_arr):
    coordinates = set()
    for index, value in np.ndenumerate(np_arr):
        if value == '#':
            coordinates.add(index)
    return coordinates


def get_distances(coords, expansion_rate):
    total_distances = 0
    for galaxy in coords:
        for next_galaxy in coords:
            x_difference = [galaxy[0], next_galaxy[0]]
            x_difference.sort()
            y_difference = [galaxy[1], next_galaxy[1]]
            y_difference.sort()
            vert_count = abs(x_difference[0] - x_difference[1])
            hor_count = abs(y_difference[0] - y_difference[1])
            for r in empty_rows:
                if r in range(x_difference[0] + 1, x_difference[1]):
                    vert_count += expansion_rate - 1
            for c in empty_cols:
                if c in range(y_difference[0] + 1, y_difference[1]):
                    hor_count += expansion_rate - 1
            total_distances += vert_count + hor_count
    return int(total_distances/2)


# Part 1
print(get_distances(find_galaxies(universe), 2))

# Part 2
print(get_distances(find_galaxies(universe), 1000000))

