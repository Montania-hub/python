with open('text5.txt', 'w+') as f:
    f.write(input('введите числа через пробел - '))
    f.seek(0)
    print(sum(map(int, f.readline().split())))


