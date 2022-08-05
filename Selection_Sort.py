# Selection sort
my_list = [5, 3, 8, 6, 7, 2]
# print(min(my_list))
# print(max(my_list))


def sort(nums):
    for i in range(len(nums)-1):
        minpos = i
        for j in range(i, len(nums)):
            if nums[j] < nums [minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        print(nums)


print("Before: ", my_list)
sort(my_list)
print("After Selection Sorting: ", my_list)
