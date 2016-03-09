from os.path import join, basename

START_YEAR = 1950
END_YEAR = 2015
DATA_DIR = 'tempdata'

for year in range(START_YEAR, END_YEAR, 5):
	thefilename = join(DATA_DIR, 'yob' + str(year) + '.txt')
	names_dict = {}
	thefile =  open(thefilename, 'r')
	for line in thefile:
		name, gender, count = line.split(',')
		if not names_dict.get(name):
			names_dict[name] = {'M': 0, 'F': 0}
		names_dict[name][gender] += int(count)

	thefile.close()

	# names_dict now contains a dict of dicts:
	# {
	#    'Jennifer': {'F': 24222, 'M': 32},
	#    'Amanda':   {'F': 10000, 'M': 0 },
	#    'John':     {'F': 12,    'M': 12000}
	# }

	total_namecount = len(names_dict.keys())
	total_babycount = 0
	for v in names_dict.values():
		totes = v['M'] + v['F'] # count up males and females
		total_babycount += totes

	print(year)
	print("Total:", round(total_babycount / total_namecount), 'babies per name')
# for boys and girls separately
	for interval in ['M', 'F']:
		babycount = 0
		namecount = 0
		for v in names_dict.values():
			if v[interval] > 0:
				babycount += v[interval]
				namecount += 1
		print("    %s:" % interval, round(babycount / namecount), 'babies per name')