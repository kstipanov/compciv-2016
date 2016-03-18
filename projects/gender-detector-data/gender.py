from os.path import join
import json
DATA_DIR = 'data'
WRANGLED_JSON_FILENAME = join(DATA_DIR, 'wrangledbabynames.json')

NAMES_DATA_ROWS = json.load(open(WRANGLED_JSON_FILENAME))

def detect_gender(name):
    # preparing an empty result just in case the given name is not found in our database
    result = { 'name': name, 'gender': None, 'ratio': None, 'males': 0, 'females': 0, 'total': 0 }
    for row in NAMES_DATA_ROWS:
        # find first row...
        if name.lower() == row['name'].lower():
            # this should be the match
            result = row
            # since each name only shows up once in our list
            # we can break early rather than iterating through the rest of NAMES_DATA_ROWS
            break
    # if no match was found, result is what it was at the beginning
    return result