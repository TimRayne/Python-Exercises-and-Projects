set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

if set1.isdisjoint != True:
    print('Two sets have items in common')
    set3 = set1.intersection(set2)
    print(set3)