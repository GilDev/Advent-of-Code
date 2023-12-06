import fileinput
from collections import namedtuple

# ----- With named tuples ----- #

# I prefer this method, it is more readable despite being longer and more litteral.

Symbol = namedtuple('Symbol', ('c', 'y', 'x'))
symbols = []
Number = namedtuple('Number', ('value', 'y', 'start', 'end'))
numbers = []
tot1 = 0
tot2 = 0

# Get symbols and numbers coordinates
for y, line in enumerate(fileinput.input()):
	number = ''
	for x, c in enumerate(line):
		if not c.isdigit() and c != '.' and c != '\n':
			symbols.append(Symbol(c, y, x))

		if c.isdigit():
			number += c
		elif number:
			numbers.append(Number(int(number), y, x - len(number), x - 1))
			number = ''

for symbol in symbols:
	adj = []
	for number in numbers:
		if number.y - 1 <= symbol.y <= number.y + 1 and number.start - 1 <= symbol.x <= number.end + 1:
			tot1 += number.value

			if symbol.c == '*':
				adj.append(number)

	if len(adj) == 2: # This symbol is a gear
		tot2 += adj[0].value * adj[1].value

print("Part 1:", tot1)
print("Part 2:", tot2)



# ----- Part 1 with tuples ----- #

# symbols = []
# numbers = []
# tot = 0

# # Get symbols and numbers coordinates
# for y, line in enumerate(fileinput.input()):
# 	number = ''
# 	for x, c in enumerate(line):
# 		if not c.isdigit() and c != '.' and c != '\n':
# 			symbols.append((y, x))

# 		if c.isdigit():
# 			number += c
# 		elif number:
# 			numbers.append((int(number), y, x - len(number), x - 1))
# 			number = ''

# for y, x in symbols:
# 	for number, yy, start, end in numbers:
# 		if yy - 1 <= y <= yy + 1 and start - 1 <= x <= end + 1:
# 			tot += number

# print(tot)
