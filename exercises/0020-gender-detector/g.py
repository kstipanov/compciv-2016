from os.path import join, basename
import csv

DATA_DIR = 'tempdata'
WRANGLED_HEADERS = ['year', 'name', 'gender' , 'ratio' , 'females', 'males', 'total']
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangled2014.csv')
YEAR = 2014
thefilename = join(DATA_DIR, 'yob' + str(YEAR) + '.txt')

namesdict = {}
with open(thefilename, 'r') as thefile:
    for line in thefile:
        name, gender, count = line.split(',')
        if not namesdict.get(name):
            namesdict[name] = {'M': 0, 'F': 0}
        namesdict[name][gender] += int(count)

awesome_list = []
# filling list with dicts, from dicts that are in namesdict
for name, babiescount in namesdict.items():
    xdict = {}
    xdict['year'] = YEAR
    xdict['name'] = name
    xdict['females'] = babiescount['F']
    xdict['males'] = babiescount['M']
    xdict['total'] = xdict['males'] + xdict['females']
    if xdict['females'] >= xdict['males']:
        xdict['gender'] = 'F'
        xdict['ratio'] = round(100 * xdict['females'] / xdict['total'])
    else:
        xdict['gender'] = 'M'
        xdict['ratio'] = round(100 * xdict['males'] / xdict['total'])

    # adding xdict to awesome_list
    awesome_list.append(xdict)

wfile = open(WRANGLED_DATA_FILENAME, 'w')

wcsv = csv.DictWriter(wfile, fieldnames=WRANGLED_HEADERS) 
# turns it into DictWriter object, tells it what the fieldnames are
wcsv.writeheader()
# write the headers row

def xfoo(xdict):
    return (-xdict['total'], xdict['name'])

my_final_list = sorted(awesome_list, key=xfoo)

for row in my_final_list:
    wcsv.writerow(row)
wfile.close()

finalfile = open(WRANGLED_DATA_FILENAME, 'r')
thelines = finalfile.readlines()[0:5]
for line in thelines:
    print(line.strip())