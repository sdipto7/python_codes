import re

a = 'From shahriar.rumi.dipto@g.bracu.ac.bd'
if re.search('^From.*', a):
    print('Matches!')
a = re.findall('^From.*', a)
print('The output of a is', a)


b = 'My 2 favorite numbers are 7 and 22'
b = re.findall('[0-9]+', b)
print('The output of b is', b)


c = 'From: using the: character'
c = re.findall('^F.+:', c)
print('The output of c is', c)


d = 'From: using the: character'
d = re.findall('^F.+?:', d)
print('The output of d is', d)


e = 'From shahriar.rumi.dipto@g.bracu.ac.bd'
f = re.findall('\S+@\S+', e)
print('The output of f is', f)

g = re.findall('^From (\S+@\S+)', e)
print('The output of g is', g)

h = re.findall('@([^ ]*)', e)
print('The output of h is', h)

i = re.findall('^From .*@([^ ]*)', e)
print('The output of i is', i)

j = re.findall('@(\S*)', e)
print('The output of j is', j)

k = re.findall('^From .*@(\S*)', e)
print('The output of k is', k)