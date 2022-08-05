
class A:
    def show(self):
        print('In A Show')


class B(A):
    def show(self):
        print('In B Show')


a1 = A()
a1.show()

b1 = B()
b1.show()
