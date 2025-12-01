# Part 1

index = 50
count = 0

with open('2025/inputs/day01.txt') as f:
	for instruction in f.read().split('\n'):
		direction = instruction[0]
		number = int(instruction[1:])

		if direction == 'L':
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

with open('2025/inputs/day01.txt') as f:
	for instruction in f.read().split('\n'):
		direction = instruction[0]
		number = int(instruction[1:])

		previous_index = index
		if direction == 'L':
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