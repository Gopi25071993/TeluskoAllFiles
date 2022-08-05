# Decorators
def div(a, b):
    print(a / b)


def smart_div(func):
    def inner(x, y):
        if x < y:
            x, y = y, x
        return func(x, y)
    return inner


div1 = smart_div(div)
div1(2, 4)
div1(5, 125)
