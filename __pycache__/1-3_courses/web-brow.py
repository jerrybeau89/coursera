# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#   data = mysock.recv(512)
#   if (len(data) < 1):
#     break
#   print(data.decode())
# mysock.close()

# fhand = ur.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#   print(line.decode().strip())

import urllib.request as ur, urllib.parse as up, urllib.error as ue
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

loop_count = int(input('Enter count: ')) - 1
position = int(input('Enter position: ')) - 1
end = 0
url = input('Enter - ')
html = ur.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
url = []
for link in tags:
  url.append(link.get('href'))


while end < loop_count:
  url = url[position]
  html = ur.urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser')

  tags = soup('a')
  url = []
  for link in tags:
    url.append(link.get('href'))  
  print(f'Retrieving: {url[position]}')  

  end += 1
