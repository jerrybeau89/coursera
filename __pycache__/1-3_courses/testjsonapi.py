import urllib.request as UR, urllib.parse as UP, urllib.error as UE
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


while True:
  service_address = input('Enter location (or type "quit" to exit) - ').lower()

  if service_address == 'quit': break
  elif len(service_address) < 1: break

  else:
    parms = dict()
    parms['address'] = service_address

    if api_key is not False:
      parms['key'] = api_key

    url = serviceurl + UP.urlencode(parms)
    print('Retrieving', url)

    uh = UR.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
      js = json.loads(data)
    except:
      js = None

    if not js or 'status' not in js or js['status'] != 'OK':
      print('==== Failure To Retrieve ====')
      print(data)
      continue

    ## uncomment code below to test and see data returned
    # print(json.dumps(js, indent=4))
    print('Place id', js["results"][0]["place_id"])

    
