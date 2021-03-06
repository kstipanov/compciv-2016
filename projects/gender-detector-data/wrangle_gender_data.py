from os.path import join, basename
import csv
import json

DATA_DIR = 'data'
WRANGLED_HEADERS = ['name', 'gender' , 'ratio' , 'females', 'males', 'total']
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangledbabynames.csv')
START_YEAR = 1950
END_YEAR = 2014
years = list(range(START_YEAR, END_YEAR, 10))
years.append(END_YEAR)

namesdict = {}
for year in years:
    filename = join(DATA_DIR, 'yob' + str(year) + '.txt')
    print("Parsing", filename)
    with open(filename, 'r') as thefile:
        for line in thefile:
            name, gender, count = line.split(',')
            if not namesdict.get(name):
                namesdict[name] = {'F': 0, 'M': 0}

            namesdict[name][gender] += int(count)

my_awesome_list = []

for name, babiescount in namesdict.items():
    xdict = {'name': name, 'females': babiescount['F'], 'males': babiescount['M']}
    xdict['total'] = xdict['males'] + xdict['females']
    if xdict['females'] >= xdict['males']:
        xdict['gender'] = 'F'
        xdict['ratio'] = round(100 * xdict['females'] / xdict['total'])
    else:
        xdict['gender'] = 'M'
        xdict['ratio'] = round(100 * xdict['males'] / xdict['total'])
    my_awesome_list.append(xdict)

wfile = open(WRANGLED_DATA_FILENAME, 'w')
wcsv = csv.DictWriter(wfile, fieldnames=WRANGLED_HEADERS)
wcsv.writeheader()


def xfoo(xdict):
    return (-xdict['total'], xdict['name'])

for row in sorted(my_awesome_list, key=xfoo):
    wcsv.writerow(row)
wfile.close()

#changes into json
WRANGLED_CSV_FILENAME = join(DATA_DIR, 'wrangledbabynames.csv')
WRANGLED_JSON_FILENAME = join(DATA_DIR, 'wrangledbabynames.json')
with open(WRANGLED_CSV_FILENAME, 'r') as rfile:
    datarows = list(csv.DictReader(rfile)) 
for r in datarows:
    r['total'] = int(r['total'])
    r['males'] = int(r['males'])
    r['females'] = int(r['females'])
    r['ratio'] = int(r['ratio'])

myjsonfile = open(WRANGLED_JSON_FILENAME, 'w')
jsontext = json.dumps(datarows, indent=2)
myjsonfile.write(jsontext)
myjsonfile.close()

