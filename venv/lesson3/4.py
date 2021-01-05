def my_func(x, y):
    z = x**y
    return z

print(my_func(3, -2))

def my_func_2(x, y):
    i = 1
    z = 1/x
    while (i+1) <= abs(y):
        z = z*(1/x)
        i += 1
    return z

print(my_func_2(3, -2))