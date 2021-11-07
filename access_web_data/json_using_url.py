#Assignment 2 of week 6
import json
import urllib.request, urllib.parse, urllib.error

url = 'http://py4e-data.dr-chuck.net/comments_456958.json'
data = urllib.request.urlopen(url).read()

info = json.loads(data)
info = info['comments']

total = 0
for item in info:
    total += int(item['count'])

print(total)
