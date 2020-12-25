number = int(input('Введите натуральное число - '))
maximum = number % 10
number = number//10
while number > 0:
    if number % 10 > maximum:
        maximum = number % 10
    number = number//10
print('Максимальная цифра - ' + str(maximum))
