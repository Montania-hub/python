def int_func(text):
    text2 = text[0].upper() + text[1:]
    return text2


a = input('Введите, пожалуйста, слова, разделяя их пробелом - ')
a = a.split()

for i, el in enumerate(a):
    a[i] = int_func(el)

print(*a)
