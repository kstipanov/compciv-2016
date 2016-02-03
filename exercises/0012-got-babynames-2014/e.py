import os

name = os.path.join('tempdata', "ssa-babynames-nationwide-2014.txt")

totalfemalebabies = 0
totalmalebabies = 0
with open(name) as text:
	for line in text:
		name, sex, babies = line.strip().split(',')
		if sex == 'F':
			totalfemalebabies = totalfemalebabies + int(babies)
		elif sex =='M':
			totalmalebabies = totalmalebabies + int(babies)

print("F: ", totalfemalebabies)
print("M: ", totalmalebabies)