class Computer:

    def __init__(self):
        self.name = 'Gopi'
        self.age = 29

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


com1 = Computer()
com2 = Computer()
com2.age = 30
if com1.compare(com2):
    print('They are same')
else:
    print('They are different')
