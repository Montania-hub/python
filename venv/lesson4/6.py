from itertools import cycle, count
a = int(input("Начинаем счетчик с - "))
for el in count(a):
    print(el)
    if el > a+10:
        break

i = 0
for el in cycle(['q', 'w', 'e']):
    print(el)
    if i > a:
        break
    i += 1