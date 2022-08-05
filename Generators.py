# Generator
def top_ten():
    n = 1
    while n <= 10:
        sq = n*n
        yield sq
        n += 1


values = top_ten()
# print(values)
# print(values.__next__())
# print(values.__next__())
# print(values.__next__())
# print(values.__next__())
for i in values:
    print(i)
