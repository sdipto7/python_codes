class Dog:
    x = None
    name = None

    def __init__(self, n):
        self.name = n
        self.x = 0
        print(self.name, 'is created')

    def bark(self):
        self.x += 1
        print(self.name, 'barked', self.x, 'time')


class Puppy(Dog):
    points = 0

    def touchdown(self):
        self.points += 7
        self.bark()
        print(self.name, 'barked', self.x, 'times')


d1 =Dog('Rocky')
d1.bark()
d2 = Puppy('Courage')
d2.bark()
d2.touchdown()
d2.bark()