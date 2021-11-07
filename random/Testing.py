#
# def do_math(a,b,kind='add'):
#     print(kind)
#     if(kind == 'add'):
#         return a+b
#     else:
#         return b-a
# print(do_math(5, 3))


# print(type(1))
# print(type(1.0))
# print(type(do_math))


# x = (1,"two",3,"four")
# print(x)
# # print(x[1])
# print(type(x))
# for i in x:
#     print(i)


# item = [1,2,3,5.0]
# print(item)
# item = item+[7,10,13,15.0]
# i=0
# while (i != len(item)):
#     print(item[i])
#     i=i+1
# item = item * 2
# print(item)
# print(5.0 in item)
# print(max(item))


# string = "this is a string"
# print(string[-5])
# string = string + " !"
# print(string + " !")


# x = "Shahriar Rumi Dipto".split(' ') [0]
# y = "Shahriar Rumi Dipto".split(' ') [-1]
# print(x)
# print(y)
# print(x+ " " +y)


# x = {"Dipto" : "shahriardipto7@gmail.com" , "Oshru" : "priataoshru@gmail.com"}
# print(x["Dipto"])
# print(x["Oshru"])

# for i in x:
#     print(i)
#     print(x[i])

# for i in x.values():
#     print(i)

# for i , j in x.items():
#     print(i)
#     print(j)

# x = ["Shahriar" , "Dipto"]
# fName , lName = x
# print(fName)
# print(lName)


# string = "You are {} years old"
# x = input("how old are you?")
# print(string.format(x))


peoples = ["Dr. Christopher Brooks", "Dr. Kevyn Collins-Thompson", "Dr. Vinod Sharma"]

def split_title_and_name(person):
    return "{} {}".format(person.split()[0],person.split()[-1])

# print(list(map(split_title_and_name, peoples)))

# for person in peoples:
#     print(split_title_and_name(person) == (lambda x: x.split()[0]+" "+x.split()[-1])(person))

print(list(map(split_title_and_name,peoples)) == list(map(lambda x: x.split()[0]+ " "+ x.split()[-1],peoples)))