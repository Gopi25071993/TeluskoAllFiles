# Inner Class

class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop('Acer', 'Ryzen 3', '16 GB')

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self, brand, cpu, ram):
            self.brand = brand
            self.cpu = cpu
            self. ram = ram

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Gopi', 1993)
s2 = Student('Ranjini', 1994)

s1.show()
s2.show()
# print(id(lap1))
# print(id(lap2))
