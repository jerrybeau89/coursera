import urllib.request as UR, urllib.parse as UP, urllib.error as UE
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else:
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)
''')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("where.data")
count = 0 
stop_count = 200


def pausing(secs):
  if count % 10 == 0:
    print('Pausing for a bit...')
    time.sleep(secs)

for line in fh:
  if count > stop_count: 
    print(f'Retrieved {count} loactions, restart to retrieve more')
    break

  address = line.strip()
  print('')
  cur.execute('SELECT geodata FROM Locations WHERE address = ? ', (memoryview(address.encode()), ))

  try:
    data = cur.fetchone()[0]
    print(f'Found in database {address}')
    continue
  except:
    pass

  parms = dict()
  parms["address"] = address
  if api_key is not False: parms['key'] = api_key
  url = serviceurl + UP.urlencode(parms)

  print(f'Retrieving {url}')
  uh = UR.urlopen(url, context=ctx)
  data = uh.read().decode()
  print(f'Retieved {len(data)} characters', data[:20].replace('\n', ' '))
  count = count + 1

  try: 
    js = json.loads(data)
  except:
    print(data)
    continue

  if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
    print('==== Failure TO Retrieve ====')
    print(data)
    break

  cur.execute('''
  INSERT INTO Locations (address, geodata) VALUES ( ? ,? )
  ''', (memoryview(address.encode()), memoryview(data.encode())))

  conn.commit()

  pausing(3)

print('Run geodump.py to read the data from the database so you can visualize it on a map')
    