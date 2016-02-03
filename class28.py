import requests
import json

print("hello there!")
print("type in an adddress:")
input() = address_string

ENDPOINT_URL = 'https://maps.googleapiscom/maps/api/geocode/json'
XTHING = '?address='

FINAL_URL = ENDPOINT_URL + XTHING + address_string
resp = requests.get(FINAL_URL)

data = json.loads(resp.text)

for r in data['results']:
	xlist = []
	xlist.append(r['formatted_address'])
	xlist.append(r['geometry']['location']['lng'])
	xlist.append(r['geometry']['location']['lat'])
	print(\
