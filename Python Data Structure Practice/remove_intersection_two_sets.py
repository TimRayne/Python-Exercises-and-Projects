first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

combined = first_set.intersection(second_set)
removed = set()

for i in combined:
    if i in first_set:
        first_set.remove(i)


print("The sets intersect at:", combined)
print('First Set after removing common element:', first_set)
