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
	mylist.append(result['formatted_address'])
	for c in result['geometry']:
		for c in result['location']:
			mylist.append(str(result['lng']))
			mylist.append(str(result['lat']))
	
print(';'.join(mylist))