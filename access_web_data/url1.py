import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

##sample url

# url = "http://py4e-data.dr-chuck.net/comments_42.html"

##actual url from which data needs to retrieve from
url = 'http://py4e-data.dr-chuck.net/comments_456955.html'
html = urllib.request.urlopen(url, context=ctx).read()
bs = BeautifulSoup(html, 'html.parser')

tags = bs('span')
total = 0
for tag in tags:
    total = total + int(tag.contents[0])

print(total)