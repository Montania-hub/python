from sys import argv

script_name, output, rate, bonus = argv


def salary(a, b, c):
    return (a * b) + c


print(salary(int(output), int(rate), int(bonus)))