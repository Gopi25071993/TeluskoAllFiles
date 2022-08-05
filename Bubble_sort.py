# Bobble Sort
my_list = [5, 3, 8, 6, 7, 2]
# print(my_list)
# my_list.sort()
# print(my_list)


def sort(sort_list):
    for i in range(len(sort_list)-1, 0, -1):
        for j in range(i):
            if sort_list[j] > sort_list[j+1]:
                temp = sort_list[j]
                sort_list[j] = sort_list[j+1]
                sort_list[j+1] = temp


print(my_list)
sort(my_list)
print(my_list)
