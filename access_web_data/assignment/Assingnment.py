import re

file = open('file1.txt')
# file = open('file2.txt')
s = 0
for line in file:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    for i in x:
        s+= int(i)

print(s)

# # #Character to ASCII value - ord()
# print(ord('l'))
# print(ord('i'))
# print(ord('n'))
# print(ord('e'))
# # #ASCII value to Character - chr()
# print(chr(65))