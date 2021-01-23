with open('text1.txt', 'w') as f:
    while True:
        a = input('Введите строку или ввод, чтобы закончить - ')
        if a == '':
            break
        f.write(a + '\n')
