from os.path import join
import json
DATA_DIR = 'tempdata'
WRANGLED_FINAL_FILENAME = join(DATA_DIR, 'wrangledbabynames.json')
NAMES_DATA_ROWS = []

with open(WRANGLED_FINAL_FILENAME) as data_file:    
    NAMES_DATA_ROWS = json.load(data_file)

def detect_gender_from_json(name):
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
    result = detect_gender_from_json(name)
    print(name, result['gender'], result['ratio'])
    if result['gender']:
        namecount[result['gender']] += 1

    if result['gender'] != 'NA': 
        babycount['males'] += result['males']
        babycount['females'] += result['females']

print("Total:")
print("F:", namecount['F'], 'M:', namecount['M'], 'NA:', namecount['NA'])
print('females:', babycount['females'], 'males:', babycount['males'])