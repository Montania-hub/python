import statistics

d = {}
a = []
with open("salary.txt", encoding = 'utf-8') as file:
    for line in file:
        key, value = line.split()
        d[key] = int(value)

def get_key(val):
        for key, value in d.items():
            if val >= value:
                a.append(key)
        return a

print(f'Зарплата меньше, чем 20 000 у - {get_key(20000)}')
print(f'Средняя зарплата - {round(statistics.mean(d.values()), 2)}')

