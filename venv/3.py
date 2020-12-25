number = int(input('Введите, пожалуйста, цифру - '))
while number < 0 or number > 10:
    print('Это не цифра. Повторите попытку!')
    number = int(input('Введите, пожалуйста, цифру снова - '))
print('Искомая сумма равна - ' + str(number*123))
