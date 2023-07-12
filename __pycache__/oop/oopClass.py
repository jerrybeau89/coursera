class PartyAnimal:
  x = 0
  name = ''
  def __init__(self, z):
    self.name = z
    print(self.name, "constructed")

  def party(self):
    self.x = self.x +1
    print(self.name, 'party count', self.x)
  
  def sleep(self):
    print(self.name, "is tired!")

  def __del__(self):
    print(self.name, "destructed", self.x)


class FootballFan (PartyAnimal):
  points = 0 
  def touchdown(self):
    self.points = self.points + 7
    print(self.name, 'points', self.points)
    self.party()

b = FootballFan('Beau')

b.touchdown()
b.touchdown()
b.touchdown()




