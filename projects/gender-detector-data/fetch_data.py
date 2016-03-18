import requests
from os import makedirs
from os.path import join
from shutil import unpack_archive
from glob import glob

SOURCE_URL = 'https://raw.githubusercontent.com/cmoa/collection/master/cmoa.json'
DATA_DIR = 'tempdata'
DATA_ZIP_PATH = join(DATA_DIR, 'carnegie_collection.json')

makedirs(DATA_DIR, exist_ok=True)

print("Downloading", SOURCE_URL)
resp = requests.get(SOURCE_URL)
with open(DATA_ZIP_PATH, 'w') as f:
    f.write(resp.text)
print("Downloaded", SOURCE_URL)