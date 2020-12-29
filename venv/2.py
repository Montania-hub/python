a = []
c = input('Введите первый элемент списка - ')
a.append(c)

while True:
    print('Выберите пункт меню:\n1. Ввести следующий элемент\n2. Список закончен')
    b = input('Ваш выбор - ')
    if b == '1':
        a.append(input('Введите следующий элемент списка - '))

    else:
        break

if len(a) != 1:
    x = 1
    while x < len(a):
        a[x-1], a[x] = a[x], a[x-1]
        x += 2
print(a)
