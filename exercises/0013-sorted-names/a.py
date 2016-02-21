import requests
import os

os.makedirs("tempdata", exist_ok = True)

url = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
resp = requests.get(url)
mytext = resp.text

name = os.path.join('tempdata', "ssa-babynames-nationwide-2014.txt")

namesfile = open(name, 'w')
namesfile.write(mytext)
namesfile.close()

characters = len(mytext)
print("There are ", characters, "characters in tempdata/ssa-babynames-nationwide-2014.txt")