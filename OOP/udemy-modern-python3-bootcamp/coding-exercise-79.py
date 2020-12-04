class Chicken:

    total_eggs = 0

    def __init__(self, species, name):

        self.species = species
        self.name = name
        self.eggs = 0

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs


c1 = Chicken("alice", "test")
c2 = Chicken("bob", "testing")

print(Chicken.total_eggs)
c1.lay_egg()
print(c1.total_eggs)
c2.lay_egg()
print(c1.eggs)
print(c2.eggs)
print(Chicken.total_eggs)