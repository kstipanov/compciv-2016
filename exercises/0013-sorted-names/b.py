import os

name = os.path.join('tempdata', "ssa-babynames-nationwide-2014.txt")

records_list = []
with open(name) as text:
	for line in text:
		name, sex, babies = line.strip().split(',')
		row = [name, sex, int(babies)]
		records_list.append(row)

def sort_by_popularity(x):
	return x[2]

newlist = sorted(records_list, key=sort_by_popularity, reverse=True)

num = -1
for line in newlist:
	if num < 9:
		num += 1
		printednum = num + 1
		print (str(printednum) + ". ")
		print(newlist[num][0], newlist[num][1], newlist[num][int(2)])

