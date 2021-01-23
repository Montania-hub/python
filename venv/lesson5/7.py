import json
import statistics

with open('7.json', 'w', encoding = 'utf=8') as j:
    with open('7.txt', encoding = 'utf=8') as f:
            d = {line.split()[0]: (int(line.split()[2]) - int(line.split()[3])) for line in f}
            w = [int(i) for i in d.values() if int(i) > 0]
            a = {'average_profit': statistics.mean(w)}
            result = [d, a]
    json.dump(result, j, ensure_ascii=False)
