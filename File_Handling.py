
my_file = open('MyData_File_Handler.txt', 'r')
f = open('GLWallpaper.jpg', 'rb')
for i in f:
    print(i)

f1 = open('newGLWallpaper.jpeg', 'wb')
for i in f:
    f1.write(i)

# print(my_file)
# print(my_file.read())
# print(my_file.readline(), end='')
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline(6))

# my_file1 = open('abc_File_Handler.txt', 'w')
#
# for data in my_file:
#     my_file1.write(data)

# my_file1 = open('abc_File_Handler.txt', 'a')
# my_file1.write('Laptop ')
# my_file1.write('Today ')
# my_file1.write('is ')
# my_file1.write('Friday ')
