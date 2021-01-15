list = [100, 50, 15, 200, 150, 300]

new_list = [list[i] for i in range(1, len(list)) if list[i] > list[i-1]]
print(new_list)
