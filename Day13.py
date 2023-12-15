import numpy as np

input_file = 'InputFiles/Day13.txt'

# turn input file into numpy array
data_file = open(input_file).read().split("\n\n")
puzzles = [np.array([list(x) for x in p.split("\n")]) for p in data_file]


def check_mirror(puzzle, a, b, ax, part):
    axis = {'v': 1, 'h': 0}
    num_cols = puzzle.shape[axis[ax]]
    width = min(a, num_cols - 1 - b)
    if ax == 'v':
        sub_L = puzzle[:, (a - width):(a + 1)]
        sub_R = puzzle[:, (b):(b + width + 1)]
    else:
        sub_L = puzzle[(a - width):(a + 1), :]
        sub_R = puzzle[(b):(b + width + 1), :]

    if part == 1:
        cond = np.array_equal(sub_L, np.flip(sub_R, axis=axis[ax]))
    else:
        cond = np.sum(sub_L != np.flip(sub_R, axis=axis[ax])) == 1
    if cond:
        if ax == 'h':
            return (a + 1)*100
        else:
            return (a + 1)
    else:
        return 0


p1_sum = 0
p2_sum = 0
for puzzle in puzzles:
    p1_score = 0
    p2_score = 0
    for x in range(puzzle.shape[1] - 1):
        p1_score += check_mirror(puzzle, x, x+1, 'v', 1)
        p2_score += check_mirror(puzzle, x, x + 1, 'v', 2)
    for y in range(puzzle.shape[0] - 1):
        p1_score += check_mirror(puzzle, y, y+1, 'h', 1)
        p2_score += check_mirror(puzzle, y, y + 1, 'h', 2)
    p1_sum += p1_score
    p2_sum += p2_score

print(p1_sum)
print(p2_sum)
