## THIS IS THE ASSIGNMENT 2 OF PARSING WEB PAGE
## THIS IS THE SAMPLE DATA

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'

for i in range(4):
    html = urllib.request.urlopen(url, context=ctx).read()
    bs = BeautifulSoup(html, 'html.parser')
    tags = bs('a')
    url = tags[2].get('href')

name = tags[2].contents[0]
print(name)