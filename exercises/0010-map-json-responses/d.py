import os
import json

mapsdir = os.path.join('tempdata', 'googlemaps')
json_path = os.path.join(mapsdir, 'stanford.json')

myfile = open(json_path, 'r')
txt = myfile.read()
data = json.loads(txt)
myfile.close()

mydict = json.loads(txt)

for result in mydict['results']:
	mylist = []
	for c in result['address_components']:
		mylist.append(c['long_name']) 
	print(';'.join(mylist))

