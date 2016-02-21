import os

name = os.path.join('tempdata', "ssa-babynames-nationwide-2014.txt")

namesdict = {}
with open(name) as text:
	for line in text:
		name, sex, babies = line.strip().split(',')
		if namesdict.get(name):
			namesdict[name] += int(babies)
		else:
			namesdict[name] = int(babies)


def sort_by_char(x):
	return (len(x[0]), x[1])

bignames = {}
for name, num in namesdict.items():
	if num >= 2000:
		bignames[name] = num

for i, n in enumerate(sorted(list(bignames.items()), key = sort_by_char, reverse=True)[0:10]):
	name, count = n
	print(name.ljust(15), str(count).rjust(8))