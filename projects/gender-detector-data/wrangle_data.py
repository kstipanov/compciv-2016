from os.path import join, basename
import csv
import json
DATA_DIR = 'data'
SOURCE_DATA_FILENAME = join(DATA_DIR, 'carnegie_collection.json')
WRANGLED_HEADERS = ['title', 'creation_date', 'date_acquired', 'cited_name', 'party_type']
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangled_carnegie_collection.csv')


with open (SOURCE_DATA_FILENAME, "r") as f:
    original_data = json.load(f)

wf = open(WRANGLED_DATA_FILENAME, 'w')
cwf = csv.DictWriter(wf, fieldnames=WRANGLED_HEADERS)
cwf.writeheader()

things = original_data['things']
for i in things:
#    print(i['title'], i['creation_date'])
    d = {}
    d['title'] = i['title']
    d['creation_date'] = i['creation_date']
    if i['creation_date']:
        if 'c. ' in d['creation_date']:
            d['creation_date'] = d['creation_date'][2:]
    if i['date_acquired']:
        d['date_acquired'] = i['date_acquired'][:4]

    creators = i.get('creator')
    if creators:
        for creator in creators:
            if creator['party_type'] == 'Person' and "unknown" not in creator['cited_name'].lower():
                d['cited_name'] = creator["cited_name"]
                cwf.writerow(d)
            
    else:
        pass

        #split by comma, space. 
