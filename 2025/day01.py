import os

day = int(os.path.basename(__file__)[3:5])

with open(f"2025/inputs/day{day:02}.txt") as f:
    instructions = f.read().split("\n")

# Part 1

index = 50
count = 0

for instruction in instructions:
    direction = instruction[0]
    number = int(instruction[1:])

    if direction == "L":
        index -= number
    else:
        index += number

    index %= 100

    if index == 0:
        count += 1

print(f"Part 1: {count}")

# Part 2

index = 50
count = 0

for instruction in instructions:
    direction = instruction[0]
    number = int(instruction[1:])

    previous_index = index
    if direction == "L":
        index -= number
    else:
        index += number

    if index == 0:
        count += 1
    elif index >= 100:
        count += index // 100
    elif index < 0:
        count += index // -100 + (previous_index != 0)

    index %= 100

print(f"Part 2: {count}")
