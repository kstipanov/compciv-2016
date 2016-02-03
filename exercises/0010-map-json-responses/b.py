from os.path import join
import json

JSON_PATH = join('tempdata', 'googlemaps', 'stanford.json')

myfile = open(JSON_PATH, 'r')
text = myfile.read()
mydict = json.loads(text)
myfile.close()

print(mydict['status'])