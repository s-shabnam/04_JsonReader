#Calling a JSON API
#In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/geojson.py.
# The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.


from urllib.parse import urlencode
from urllib.request import urlopen
import json

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urlencode({'sensor':'false', 'address': address})
    print('Retrieving', url)
    data = urlopen(url).read().decode('utf-8')
    print('Retrieved',len(data),'characters')

    try: js = json.loads(str(data))

    except:
        js = None
        print('Could not read JSON file :((')
        exit()

    #print(json.dumps(js, indent=4))
    print('Here the corresponding place_id : ', js['results'][0]['place_id'])
