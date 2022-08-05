# Poly - Many
# morphism - Form
# ============================
# Duck Typing
# Operator overloading
# Method overloading
# Method Overriding
# ============================
"""
Duck Typing
"""
# x = 5
# print(type(x), id(x))
# x = 'Gopi'
# print(type(x), id(x))
class PyCharm:
    def execute(self):
        print('Compiling', "\nRunning")


class MyEditor:
    def execute(self):
        print('Spell check')
        print('Convention check')
        print('Compiling', "\nRunning")


class Laptop:
    def code(self, ide):
        ide.execute()


ide = PyCharm()
ide1 = MyEditor()

lap1 = Laptop()
lap1.code(ide)
lap1.code(ide1)
