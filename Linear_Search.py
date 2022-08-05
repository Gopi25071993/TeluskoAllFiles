my_list = [5, 8, 4, 6, 9, 2]
n = 9
pos = -1


def search(searchlist, number):
    i = 0
    while i < len(searchlist):
        if searchlist[i] == number:
            globals()['pos'] = i
            return True
        i += 1
    return False


def search1(searchlist, number):
    for sl in searchlist:
        if sl == number:
            globals()['pos'] = searchlist.index(sl)
            return True
    return False


if search1(my_list, n):
    print('Found at', pos+1)
else:
    print('Not Found')
