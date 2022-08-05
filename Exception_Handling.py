a = 5
b = 2
try:
    print('Resource open')
    print(a/b)
    k = int(input('Enter a number'))
    print(a/k)
    print('Resource Closed TRY')
except ZeroDivisionError as e:
    print('Hey you cannot divide by Zero: ', e)
except ValueError as e:
    print('Invalid Input')
except Exception as e:
    print('', e)
finally:
    print('Finally executed')
    print('Resource Closed')

print('Bye')
