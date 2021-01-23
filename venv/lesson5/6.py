import re
d = {}
with open('6.txt', encoding = 'utf-8') as f:
    for line in f:
        subject, other = line.split(':')
        num = re.compile('\d+')
        hours = num.findall(other)
        d[subject] = sum(map(int, hours))
print(d)
