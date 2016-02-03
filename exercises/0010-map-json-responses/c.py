from os.path import join
import json

JSON_PATH = join ('tempdata', 'googlemaps', 'stanford.json')

myfile = open(JSON_PATH, 'r')
text = myfile.read()
data = json.loads(text)
myfile.close()

for result in data ['results']:
	print(result['formatted_address'])