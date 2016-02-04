import os
import json

mapsdir = os.path.join('tempdata', 'mapzen')
json_path = os.path.join(mapsdir, 'stanford.json')

myfile = open(json_path, 'r')
text = myfile.read()
mydict = json.loads(text)
myfile.close()

print("type: ", mydict['type'])

for i in mydict['geocoding']:
	a = ['query']['text']
	b = ['query'][str('size')]
	c = ['query']['boundary.country']

print("text: ", a)
print("size: ", b)
print("boundary.country: ", c)


	