a = float(input('Введите длину первой пробежки в км - '))
b = float(input('Введите целевую длину дистанции в км - '))

x = 1
while a*(1.1**(x-1)) < b:
    if a*(1.1**x) < b:
        x += 1
    else:
        break
print('Нужно ' + str(x) + ' дней')
