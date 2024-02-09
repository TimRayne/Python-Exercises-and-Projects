dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

for i in dict2:
    if i not in dict1:
        key = str(i)
        val = dict2[i]
        dict1[key] = val

print(dict1)

