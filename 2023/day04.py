import fileinput
from collections import Counter

tot1 = 0
tot2 = 0
scratchcards = Counter()

for line in fileinput.input():
	game, record = line.strip().split(': ')
	game_id = int(game[5:])

	nb_winning_numbers = 0
	scratchcards[game_id] += 1

	winning, your = record.split(' | ')

	winning_numbers = [int(n) for n in winning.split()]
	numbers = [int(n) for n in your.split()]

	for number in numbers:
		if number in winning_numbers:
			nb_winning_numbers += 1

	if nb_winning_numbers > 0:
		tot1 += 2 ** (nb_winning_numbers - 1)

	for scratchcard in range(game_id + 1, game_id + 1 + nb_winning_numbers):
		scratchcards[scratchcard] += scratchcards[game_id]

print("Part 1:", tot1)
print("Part 2:", sum(scratchcards.values()))
