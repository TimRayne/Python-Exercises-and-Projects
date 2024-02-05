sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
c = dict()

for i in sample_list:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1

print('Count of each item ', c)