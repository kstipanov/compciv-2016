import os

name = os.path.join('tempdata', "ssa-babynames-nationwide-2014.txt")

babies = 0
with open(name) as text:
	for line in text:
		babies += int(line.split(',')[2])

print("There are", babies,"babies whose names were recorded in 2014.")

