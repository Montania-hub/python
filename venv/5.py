a = [10, 8, 7, 5, 5, 3, 1]
x = input('Введите натуральное число для добавления в список - ')
while x.isdigit() is False or int(x) < 0:
    x = input('Введите натуральное число для добавления в список - ')
i = 0
while int(x) < a[i]:
    i += 1
else:
    a.insert(i, int(x))
print(a)
