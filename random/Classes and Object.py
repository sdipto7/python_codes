class Dog:
    x = None
    name= None
    def __init__(self, n):
        self.name = n
        self.x = 0

    def bark(self):
        self.x = self.x + 1
        print(self.name,'barked', self.x,'times')

    def getName(self):
        return self.name

    def __del__(self):
        print('I am done with', self.name)


d1 = Dog('Tommy')
d1.bark()
x = 10
print(x)
d1.bark()
d2 = Dog('Rocky')
d2.bark()
d1.bark()
print(d1.getName())