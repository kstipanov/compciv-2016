import requests
import json
URL = 'http://wwww.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json'
txt = requests.get(URL).text
type(txt)
