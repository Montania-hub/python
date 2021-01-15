list = [1, 1, 3, 67, 100, 100, 1]

new_list = [list[i] for i in range(0, len(list)) if list[i] not in (list[:i]+list[i+1:])]

print(new_list)

