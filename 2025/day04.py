import os
day = int(os.path.basename(__file__)[3:5])

with open(f"2025/inputs/day{day:02}.txt") as f:
    raw_input = f.read().split("\n")

matrix = [[c for c in row] for row in raw_input]

# Nothing very fancy or optimized today, just simple brute force that is still fast enough to compute

# Part 1

def neighbors_count(matrix, x, y):
    neighbors = 0
    for j in range(y-1, y+2):
        if j < 0 or j >= len(matrix):
            continue

        for i in range(x-1, x+2):
            if i < 0 or i >= len(matrix[0]) or (j == y and i == x):
                continue

            if matrix[j][i] == "@":
                neighbors += 1

    return neighbors

total = 0

for y, row in enumerate(matrix):
    for x, c in enumerate(row):
        if c == "@" and neighbors_count(matrix, x, y) < 4:
            total += 1

print(f"Part 1: {total}")

# Part 2

total = 0

removed = True
while removed:
    removed = False
    for y, row in enumerate(matrix):
        for x, c in enumerate(row):
            if c == "@" and neighbors_count(matrix, x, y) < 4:
                total += 1
                matrix[y][x] = "x"
                removed = True

print(f"Part 2: {total}")
