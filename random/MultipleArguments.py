'''
Using 'args' as the variable is a good practice for python developers.
putting a '*' before any variable means it can take multiple parameters.
'''
def addNumber(*args):
    sum = 0
    for x in args:
        sum += x
    print(sum)
addNumber(3)
addNumber(1,1,1)
addNumber(5,6,7,8,9,10)