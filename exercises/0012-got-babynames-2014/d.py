import os

name = os.path.join('tempdata', "ssa-babynames-nationwide-2014.txt")

femalenum = 0
malenum = 0

with open(name) as text:
	for line in text:
		name, sex, babies = line.strip().split(',')
		if sex == 'F':
			if femalenum == 0:
				print("Top baby girl names")
			if femalenum < 5:
				femalenum += 1
				print(name, ": ", babies)
		elif sex == 'M':
			if malenum == 0:
				print ("\n")
				print("Top baby boy names")
			if malenum < 5:
				malenum += 1
				print(name, ": ", babies)