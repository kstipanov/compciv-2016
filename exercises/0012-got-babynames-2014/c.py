import os

name = os.path.join('tempdata', "ssa-babynames-nationwide-2014.txt")

Daenerys = 0
Khaleesi = 0
with open(name) as text:
	for line in text:
		name, sex, babies = line.strip().split(',')
		if sex == 'F':
			if name == 'Daenerys':
				Daenerys += int(babies)
			elif 'Khalees' in name or 'Khaless' in name:
				Khaleesi += int(babies)

print("Daenerys: ", Daenerys)
print("Khaleesi: ", Khaleesi)
