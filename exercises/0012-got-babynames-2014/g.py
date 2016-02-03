import os
import string

name = os.path.join('tempdata', "ssa-babynames-nationwide-2014.txt")

m_dict = {}
f_dict = {}

with open(name) as text:
	for line in text:
		name, sex, babies = line.strip().split(',')
		last_letter = name[-1]
		if sex == 'F':
			if f_dict.get(last_letter):
				f_dict[last_letter] += int(babies)
			else:
				f_dict[last_letter] = int(babies)
		else:
			if m_dict.get(last_letter):
				m_dict[last_letter] += int(babies)
			else:
				m_dict[last_letter] = int(babies)

print("letter", "F".rjust(10, ' '), "M".rjust(7, ' '))
print("-------------------------")
for letter in string.ascii_lowercase:
	mval = str(m_dict[letter])
	fval = str(f_dict[letter])
	print(letter, (fval.rjust(15, ' ')), (mval.rjust(7, ' ')))