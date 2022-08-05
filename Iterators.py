# my_list = [7, 8, 9, 5]
# # print(my_list[7])
#
# # for i in my_list:
# #     print(i)
# it = iter(my_list)
# # print(it)
# print(it.__next__())
# print((next(it)))
# # print(it.__next__())
# # print(it.__next__())
# for i in my_list:
#     print(i)

class Top10:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


values = Top10()
print(values)
print(values.__next__())
print(values.__next__())

for i in values:
    print(i)
