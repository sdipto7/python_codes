file = open('input.txt','r')
info = file.read()
words=""
for i in info:
    words = info.split()


#b = 0
#for i in words:
    #print(words[b])
    #b+=1

for i in words:
    print(i)

#if "fi" in keyword:
    #print("yes")
