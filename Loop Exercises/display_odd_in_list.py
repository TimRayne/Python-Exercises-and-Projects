my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = 0
for num in my_list:
    if index % 2 == 0:
        index += 1
        continue
    else:
        index += 1
        print(num)