class Fruit:
    name = ""
    poisonous = False

    def __init__(self, nameofFruit, poisonous):
        self.name = nameofFruit
        self.poisonous = poisonous
    def describe(self):
        print self.name


f1 = Fruit('apple',True)
f2 = Fruit('banana', False)

f1.describe()
f2.describe()
