import os
import json

mapsdir = os.path.join('tempdata', 'mapzen')
json_path = os.path.join(mapsdir, 'stanford.json')

myfile = open(json_path, 'r')
text = myfile.read()
mydict = json.loads(text)
myfile.close()

print("type: ", mydict['type'])

query_dict = mydict['geocoding']['query']

print("text: ", query_dict['text'])
print("size: ", query_dict['querySize'])
print("boundary.country: ", query_dict['boundary.country'])


	