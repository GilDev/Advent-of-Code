import fileinput
from collections import namedtuple

maps = []

def convert(maps, source):
	for map in maps:
		for destination_start, source_start, length in map:
			if source_start <= source <= source_start + length:
				source += destination_start - source_start
				break

	return source

file = ''.join(fileinput.input())
seeds, *raw_maps = file.split('\n\n')
seeds = [int(n) for n in seeds.split()[1:]]

for raw_map in raw_maps:
	lines = raw_map.split('\n')[1:]
	map = [[int(i) for i in line.split()]  for line in lines]
	maps.append(map)

print("Part 1:", min([convert(maps, seed) for seed in seeds]))

# The following won't work for big inputs, the problem has to be solved in reverse
#print("Part 2:", min([min([convert(maps, seed) for seed in range(seeds[i], seeds[i] + seeds[i + 1])]) for i in range(0, len(seeds), 2)]))
