# Construtor in Inheritance
# Method Resolution Order ==> MRO
class A:
    def __init__(self):
        print('In A init')

    def feature1(self):
        print('A: Feature 1 working')

    def feature2(self):
        print('Feature 2 working')


class B:

    def __init__(self):
        # super().__init__()
        print('In B Init')

    def feature1(self):
        print(' B: Feature 1 working')

    def feature4(self):
        print('Feature 4 working')


class C(A, B):
    def __init__(self):
        super().__init__()
        print('In C Init')

    def feat(self):
        super().feature2()


a1 = A()
b1 = B()
c1 = C()

a1.feature1()
b1.feature1()
c1.feature1()

c1.feat()