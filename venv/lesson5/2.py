with open('text1.txt', 'r') as f:
    print(f'{len(f.readlines())} - количество строк, количество слов в каждой:')

for line in open('text1.txt', 'r'):
    print(len(line.split()))
