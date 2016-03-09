from os.path import join, basename

YEAR = 2014
DATA_DIR = 'tempdata'
thefilename = join(DATA_DIR, 'yob' + str(YEAR) + '.txt')

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

print("Total:", total_namecount, 'unique names for', total_babycount, 'babies')

for gender in ['M', 'F']:
    ncount = 0
    bcount = 0
    for v in names_dict.values():

        if v[gender] > 0:
            bcount += v[gender]
            ncount += 1
    print("    %s:" % gender, ncount, "unique names for", bcount, "babies")