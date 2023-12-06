import fileinput

def getFirstAndLastDigitsConcatened(line):
	first = last = ""
	for c in line:
		if c.isdigit():
			first = c
			break

	for c in reversed(line):
		if c.isdigit():
			last = c
			break

	return int(first + last)

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digitsReversed = ["".join(reversed(digit)) for digit in digits]

def getFirstAndLastDigitsConcatenedWithSpelledOut(line):
	first = last = ""

	for firstPos, c in enumerate(line):
		if c.isdigit():
			first = c
			break

	minimum = 1000
	for i, digit in enumerate(digits):
		try:
			index = line.index(digit)
			if index < firstPos and index < minimum:
				minimum = index
				first = str(i + 1)

		except ValueError as e:
			pass

	reversedLine = "".join(reversed(line))
	for lastPos, c in enumerate(reversedLine):
		if c.isdigit():
			last = c
			break

	minimum = 1000
	for i, digit in enumerate(digitsReversed):
		try:
			index = reversedLine.index(digit)
			if index < lastPos and index < minimum:
				minimum = index
				last = str(i + 1)

		except ValueError as e:
			pass

	return int(first + last)

total = totalWithLetters = 0
for line in fileinput.input():
	total += getFirstAndLastDigitsConcatened(line)
	totalWithLetters += getFirstAndLastDigitsConcatenedWithSpelledOut(line)

print(total, totalWithLetters)
