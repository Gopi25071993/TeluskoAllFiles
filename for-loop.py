# x = ['Gopi', 65, 2.5]
x = 'GOPI'
for i in x:
    print(i)

for i in range(10):
    print(i, end=' ')

y = [i for i in range(5)]
print(y)

for i in range(1, 21):
    if i % 5 == 0:
        continue
    print('i= ', i)
