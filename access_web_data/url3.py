## THIS IS THE ASSIGNMENT 2 OF PARSING WEB PAGE
## THIS IS THE ACTUAL DATA ASKED FOR

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
# import ssl

# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Rylay.html'
# url = 'http://py4e-data.dr-chuck.net/known_by_Yasemin.html'

for i in range(7):
    html = urllib.request.urlopen(url).read()
    bs = BeautifulSoup(html,'html.parser')
    tags = bs('a')
    url = tags[17].get('href')

name = tags[17].contents[0]
print(name)

