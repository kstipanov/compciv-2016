import requests
import json

def geocode(location):
    """
      
      ____________
    < "I am a cow" >
      ------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/
                    ||----w |
                    ||     ||

    Whats up docstring?
    """
    rawtext = fetch_mapzen_response(location)
    mydict = parse_mapzen_response(rawtext)
    # add the location string to mydict
    mydict['query_string'] = location 
    # return the diccionary
    return mydict

def fetch_mapzen_response(location):
    """
    `location` is a string that will be passed onto Mapzen API for geocoding

    returns a text string containing JSON-formatted data from Mapzen
    """
    url = "https://search.mapzen.com/v1/search"
    mykey = read_mapzen_credentials()
    my_params = {'text': location, 'api_key': mykey}
    resp = requests.get(url, params = my_params)
    return resp.text

def parse_mapzen_response(txt):
    """
    `txt` is a string containing JSON-formatted text from Mapzen's API

    returns a dictionary containing the useful key/values from the most
       relevant result.
    """
    gdict = {} # just initialize a dict for now, with status of None
    data = json.loads(txt)
    if data['features']: # it has at least one feature...
        gdict['status'] = 'OK' 
        feature = data['features'][0] # pick out the first one
        props = feature['properties']  # just for easier reference
        gdict['confidence'] = props['confidence']
        gdict['label'] = props['label']

        # now get the coordinates
        coords = feature['geometry']['coordinates']
        gdict['longitude'] = coords[0]
        gdict['latitude'] = coords[1]
    else:
        gdict['status'] = None

    return gdict

def read_mapzen_credentials():
    creds_filename = "creds_mapzen.txt"
    keytxt = open(creds_filename).read().strip() # e.g. "search-blahblah"
    return keytxt