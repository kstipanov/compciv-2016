import os

name = os.path.join('tempdata', "ssa-babynames-nationwide-2014.txt")

x_list = []
with open(name) as text:
	for line in text:
		name, sex, babies = line.strip().split(',')
		if "x" in name:
			row = [name, sex, int(babies)]
			x_list.append(row)

male_x_list = []
female_x_list = []
for line in x_list:
	if x_list[1] == "M":
		male_x_list.append(line)
	elif x_list[1] == "F":
		female_x_list.append(line)

def sort_by_popularity(x):
	return x[2]

new_female_x_list = sorted(female_x_list, key=sort_by_popularity, reverse=True)
new_male_x_list = sorted(male_x_list, key=sort_by_popularity, reverse=True)

print("Female")
num = -1
for line in new_female_x_list:
	if num < 4:
		num += 1
		printednum = num + 1
		print (str(printednum) + ". ")
		print(new_female_x_list[num][0].ljust(15), new_female_x_list[num][int(2)].rjust(8))

print("Male")
num = -1
for line in new_male_x_list:
	if num < 4:
		num += 1
		printednum = num + 1
		print (str(printednum) + ". ")
		print(new_male_x_list[num][0], new_male_x_list[num][int(2)])


