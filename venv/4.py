a = input('Введите, пожалуйста,слова, разделяя их пробелом - ')
a = a.split()
for index, elem in enumerate(a, 0):
    print(index+1, elem[:10])

