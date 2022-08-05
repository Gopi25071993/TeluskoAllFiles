my_list = [4, 7, 8, 12, 45, 99]
pos = -1
n = 12


def search(search_list, num):
    low = 0
    up = len(search_list) - 1
    while low <= up:
        mid = (low + up) // 2
        if search_list[mid] == num:
            globals()['pos'] = mid
            return True
        else:
            if search_list[mid] < num:
                low = mid + 1
            else:
                up = mid - 1

    return False


if search(my_list, n):
    print('Found at ', pos+1)
else:
    print('Not Found')
