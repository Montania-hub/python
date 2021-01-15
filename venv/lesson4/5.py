from functools import reduce
list = [i for i in range(100, 1000) if i % 2 == 0]


def my_func(a, b):
    return a*b


print(reduce(my_func, list))
