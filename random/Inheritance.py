class PartyAnimal:
    x = None
    name = None

    def __init__(self, n):
        self.name = n
        self.x = 0
        print(self.name, 'is created')

    def party(self):
        self.x += 1
        print(self.name, 'party count', self.x)

class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points += 7
        self.party()
        print(self.name, 'points', self.points)

s = PartyAnimal('Sally')
s.party()
j = FootballFan('Jim')
j.touchdown()
j.party()