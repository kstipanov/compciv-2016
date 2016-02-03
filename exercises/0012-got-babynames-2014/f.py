import os
import string

name = os.path.join('tempdata', "ssa-babynames-nationwide-2014.txt")

mydict = {}
with open(name) as text:
	for line in text:
		name, sex, babies = line.strip().split(',')
		last_letter = name[-1]
		if mydict.get(last_letter):
			mydict[last_letter] += int(babies)
		else:
			mydict[last_letter] = int(babies)

for letter in string.ascii_lowercase:
	val = mydict[letter]
	print(letter, ": ", val)