import urllib.request as UR, urllib.parse as UP, urllib.error as UE
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0
count = 0
while True:
  service_url = input('Enter url (or type "quit" to exit) - ').lower()
  if service_url == 'quit': break
  elif len(service_url) < 1: break
  else:
    url = service_url
    print('Retrieving', url)
    uh = UR.urlopen(url, context=ctx)
    
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
      js = json.loads(data)
    except:
      js = None

    if not js:
      print('==== Failure To Retrieve ====')
      continue

    nums = js["comments"]
    for num in nums:
      val = int(num["count"])
      sum += val
      count += 1

    print('Count:', count)
    print('Sum:', sum)
