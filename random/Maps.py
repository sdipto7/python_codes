numbers = [1,2,3,4,5,6,7,8,9]

#this a way of filtering a list and adding values to another list
odds = []
for n in numbers:
    if n%2!=0:
        odds.append(n)
print(odds)


#the filter method filters the list and add values to another list
evens = list(filter(lambda n: n%2==0, numbers))
print(evens)


doubles = list(map(lambda x: x*2, evens))
print(doubles)


squares = list(map(lambda x: x**2, evens))
print(squares)

