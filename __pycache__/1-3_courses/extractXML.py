import urllib.request as UR, urllib.parse as UP, urllib.error as UE
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0
count = 0
while True:
    service_url = input('Enter url (or "quit" to end program) - ').lower()
    if service_url == 'quit': break

    url = service_url
    print('Retrieving', url)
    uh = UR.urlopen(url, context=ctx)

    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)

    counts = tree.findall('.//count')
    
    for nums in counts:
      num = int(nums.text)
      sum += num
      count += 1

    print('Count:', count)      
    print('Sum:', sum)
