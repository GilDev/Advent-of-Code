# Part 1

total = 0

with open("2025/inputs/day03.txt") as f:
    banks = f.read().split("\n")

for bank in banks:
    first = max(bank[:-1])
    first_index = bank.index(first)
    last = max(bank[first_index + 1 :])
    total += int(first + last)

print(f"Part 1: {total}")

# Part 2

def find_max_joltage(bank, length):
    joltage = ""
    while len(joltage) < length:
        # Find next max digit in bank while keeping the rest to fill `joltage` up to `length`
        max_digit = max(bank[:len(bank) - length + len(joltage) + 1])
        joltage += max_digit
        bank = bank[bank.index(max_digit)+1:]

    return int(joltage)

total = 0

with open("2025/inputs/day03.txt") as f:
    banks = f.read().split("\n")

for bank in banks:
    total += find_max_joltage(bank, 12)

print(f"Part 2: {total}")
