
# Instance Method
# Class Method
# Static Method

class Student:

    school = 'Telusko'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    # class methods using Decorator
    @classmethod
    def get_school(cls):
        return cls.school

    def get_n1(self):
        return self.m1

    def get_n2(self):
        return self.m1

    def get_n3(self):
        return self.m1

    def set_m1(self, value):
        self.m1 = value

    def set_m2(self, value):
        self.m2 = value

    def set_m3(self, value):
        self.m3 = value

    # Static method using Decorator
    @staticmethod
    def info():
        print('This is Student class...in ABC module')


s1 = Student(34, 67, 32)
s2 = Student(89, 32, 42)

# Instance method
print(s1.avg())
print(s2.avg())
# Class method using Decorator
print(Student.get_school())
Student.info()
