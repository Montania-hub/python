x = float(input('Enter the dividend - '))
y = float(input('Enter the divider - '))
def func(x, y):
    if y == 0:
        return 'You can not divide on 0'
    else:
        return x/y
print(func(x, y))
