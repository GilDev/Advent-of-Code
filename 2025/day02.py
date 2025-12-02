# Part 1

total = 0
ranges = []

with open('2025/inputs/day02.txt') as f:
	ranges = f.read().split(',')

for current_range in ranges:
	first, last = [int(i) for i in current_range.split('-')]

	for id in range(first, last + 1):
		id_str = str(id)
		if len(id_str) % 2 == 0 and id_str[len(id_str) // 2:] == id_str[:len(id_str) // 2]:
			total += id

print(f"Part 1: {total}")

# Part 2

total = 0
ranges = []

with open('2025/inputs/day02.txt') as f:
	ranges = f.read().split(',')

for current_range in ranges:
	first, last = [int(i) for i in current_range.split('-')]

	for id in range(first, last + 1):
		id_str = str(id)
		for length in range(1, len(id_str) // 2 + 1):
			if len(id_str) % length != 0: # Length has to be a multiple of the subsequence: no need to test "21" for string "21214"
				continue

			times = len(id_str) // length # Maximum number of repetitions in the tested string

			valid = True
			for time in range(1, times):
				if id_str[0:length] != id_str[length * time:length * (time + 1)]:
					valid = False
					break

			if valid:
				total += id
				break

print(f"Part 2: {total}")
