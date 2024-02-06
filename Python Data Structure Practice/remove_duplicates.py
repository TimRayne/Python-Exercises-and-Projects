sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
new_list = []

for i in sample_list:
    if i not in new_list:
        new_list.append(i)

new_tup = tuple(new_list)

print('List of non-duplicates:', new_list)
print('Tuple of non-duplicates:', new_tup)

smallest = min(new_tup)
largest = max(new_tup)

print('Min:', smallest)
print('Max:', largest)