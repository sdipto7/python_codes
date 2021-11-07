import json

input = '''[
{ "id" : "001", "x" : "10", "name" : "Oshru" },
{ "id" : "007", "x" : "22", "name" : "Dipto" }
] '''

info = json.loads(input)
# print(type(info))
print('User count:', len(info))
for item in info:
    print('Name:', item['name'])
    print('Id:',item['id'])
    print('Atrribute:', item['x'])