import urllib.request, urllib.parse, urllib.error, ssl
from bs4 import BeautifulSoup
count = 0

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen(input('Enter - '), context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# count paragraph
tags = soup('p')
for tag in tags:
    count = count + 1

print('paragraph count:', count)