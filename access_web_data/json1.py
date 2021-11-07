import json

data = '''{
    "name" : "Dipto",
    "phone" : { "type" : "intl", "number" : "01861770460" },
    "email" : { "hide" : "yes" }
} '''

info = json.loads(data)
# print(type(info))
print('Name:', info['name'])
print('Hide:', info['email']['hide'])