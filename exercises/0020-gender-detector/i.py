from os.path import join
import csv
DATA_DIR = 'tempdata'
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangled2014.csv')


rfile = open(WRANGLED_DATA_FILENAME, 'r')
datarows = list(csv.DictReader(rfile))

for r in datarows:
	r['total'] = int(r['total'])
	r['males'] = int(r['males'])
	r['females'] = int(r['females'])
	r['ratio'] = int(r['ratio'])

bigdatarows = []
for r in datarows:
	if (r['total'] > 99):
		bigdatarows.append(r)

print("Popular names in 2014 with gender ratio less than or equal to:")
for genderratio in (60, 70, 80, 90, 99):
	bigbigdatarows = sorted(bigdatarows, key=lambda r: r['total'], reverse=True)
	fxrows = [r for r in bigdatarows if r['ratio'] <= genderratio]
	names = set()
	for row in fxrows:
		names.add(row['name'])
	print("  ", genderratio, "%:", len(names), "/", len(bigdatarows))