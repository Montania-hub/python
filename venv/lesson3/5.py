def sum(list):
    """Делает список числовым и возвращает сумму"""
    for i, el in enumerate(list):
        list[i] = float(el)

    x = list[0]
    j = 1
    while j+1 <= len(list):
        x = x + list[j]
        j += 1
    return x


y = 0
while True:
    a = input('Введите, пожалуйста, числа, разделяя их пробелом.\nСимвол "q" прерывает ряд для обработки - ')
    a = a.split()

    if 'q' in a:
        t = 0
        while t+1 <= len(a):
            if a[t] != 'q':
                t += 1
            else:
                break
        a = a[:t]
        print(sum(a) + y)
        break

    else:
        y = sum(a)+y
        print(y)
