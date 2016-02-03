import requests
import os

FIRSTURL = 'http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json'
firstresp = requests.get(FIRSTURL)

os.makedirs('tempdata/googlemaps', exist_ok = True)
firstdir = os.path.join('tempdata', 'googlemaps')
firstname = os.path.join(firstdir, "stanford.json")
firstfile = open(firstname, 'w')
firstfile.write(firstresp.text)
firstfile.close()
print("Downloading from: http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json")
print("Writing to: tempdata/googlemaps/stanford.json")
char_count = len(firstresp.text)

firstfile = open(firstname, 'r')
first_line_num = 0
for x in firstfile:
	first_line_num += 1
firstfile.close()

print("Wrote", first_line_num, "lines and", char_count, "characters")

SECONDURL = 'http://www.compciv.org/files/datadumps/apis/mapzen/search-stanford.json'
secondresp = requests.get(SECONDURL)

os.makedirs('tempdata/mapzen', exist_ok = True)
seconddir = os.path.join('tempdata', 'mapzen')
secondname = os.path.join(seconddir, "stanford.json")
secondfile = open(secondname, 'w')
secondfile.write(secondresp.text)
secondfile.close()
print("Downloading from: http://www.compciv.org/files/datadumps/apis/mapzen/search-stanford.json")
char_count = len(secondresp.text)

secondfile = open(secondname, 'r')
second_line_num = 0
for x in secondfile:
	second_line_num += 1
secondfile.close()

print("Wrote", second_line_num, "lines and", char_count, "characters")
