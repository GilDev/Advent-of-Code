import os

day = int(os.path.basename(__file__)[3:5])

with open(f"2025/inputs/day{day:02}.txt") as f:
    ranges, ingredients = f.read().split("\n\n")

ranges = ranges.split("\n")
ingredients = ingredients.split("\n")

ranges = [(int(i.split("-")[0]), int(i.split("-")[1])) for i in ranges]

# I find it pretty readable this way, but again this is not optimal and being
# comfortable with Python's syntax helps a lot in optimizing everything:
# https://www.reddit.com/r/adventofcode/comments/1pemdwd/comment/nsdo8ja/

# Part 1

total = 0

for ingredient in ingredients:
    for start, end in ranges:
        if start <= int(ingredient) <= end:
            total += 1
            break

print(f"Part 1: {total}")

# Part 2

total = 0


def is_overlap(range1, range2):
    start1, end1 = range1
    start2, end2 = range2
    if start2 > end1 or start1 > end2:
        return False
    return True


change = True
while change:
    change = False
    for i in range(0, len(ranges) - 1):
        for j in range(i + 1, len(ranges)):
            if is_overlap(ranges[i], ranges[j]):
                new_start = min(ranges[i][0], ranges[j][0])
                new_end = max(ranges[i][1], ranges[j][1])
                ranges.append((new_start, new_end))
                del ranges[j]
                del ranges[i]
                change = True
                break
        if change:
            break

for start, end in ranges:
    total += end - start + 1

print(f"Part 2: {total}")
