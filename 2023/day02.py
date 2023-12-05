import fileinput
from collections import Counter
from math import prod

LIMITS = {
	'red': 12,
	'green': 13,
	'blue': 14,
}

tot1 = 0
tot2 = 0

for line in fileinput.input():
	game, record = line.strip().split(': ')
	game_id = int(game[5:])

	game_possible = True
	mins = Counter()

	for turn in record.split('; '):
		for draw in turn.split(', '):
			n, color = draw.split(' ')
			n = int(n)
			if n > LIMITS[color]:
				game_possible = False

			mins[color] = max(mins[color], n)

	if game_possible:
		tot1 += game_id

	tot2 += prod(mins.values())

print(tot1)
print(tot2)



# PART 1 ONLY

# for line in fileinput.input():
# 	game, record = line.strip().split(': ')
# 	game_id = int(game[5:])

# 	for turn in record.split('; '):
# 		for draw in turn.split(', '):
# 			n, color = draw.split(' ')
# 			if int(n) > LIMITS[color]:
# 				# Impossible draw
# 				break

# 		else:
# 			continue

# 		break

# 	else:
# 		tot += game_id

# print(tot)