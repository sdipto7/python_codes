import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as et

# this is the sample url
# url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

#this is the actual data url
url = 'http://py4e-data.dr-chuck.net/comments_456957.xml'
# url = 'http://py4e-data.dr-chuck.net/comments_457060.xml'

data = urllib.request.urlopen(url).read()

tree = et.fromstring(data)
# print(len(data))

tags = tree.findall('.//count')

sum = 0
for tag in tags:
    sum += int(tag.text)

print(sum)