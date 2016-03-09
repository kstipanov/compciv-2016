from os.path import join
import csv
DATA_DIR = 'tempdata'
WRANGLED_FINAL_FILENAME = join(DATA_DIR, 'wrangledbabynames.csv')
NAMES_DATA_ROWS = list(csv.DictReader(open(WRANGLED_FINAL_FILENAME)))

for r in NAMES_DATA_ROWS:
    r['total'] = int(r['total'])
    r['males'] = int(r['males'])
    r['females'] = int(r['females'])
    r['ratio'] = int(r['ratio'])


def detect_gender_from_csv(name):
    result = { 'name': name, 'gender': 'NA', 'ratio': None, 'males': None, 'females': None, 'total': 0 }
    for row in NAMES_DATA_ROWS:
        if name.lower() == row['name'].lower():
            result = row
            break
    return result



NAMES_TO_TEST = ['Michael', 'Kelly', 'Kanye', 'THOR', 'casey', 'Arya', 'ZZZblahblah']


namecount = {'M': 0, 'F': 0, 'NA': 0}
babycount = {'males': 0, 'females': 0}
for name in NAMES_TO_TEST:
    result = detect_gender_from_csv(name)
    print(name, result['gender'], result['ratio'])
    if result['gender']:
        namecount[result['gender']] += 1

    if result['gender'] != 'NA':
        babycount['males'] += result['males']
        babycount['females'] += result['females']

print("Total:")
print("F:", namecount['F'], 'M:', namecount['M'], 'NA:', namecount['NA'])
print('females:', babycount['females'], 'males:', babycount['males'])