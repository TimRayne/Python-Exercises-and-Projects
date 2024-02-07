list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []

# website solution
list4 = [x + y for x in list1 for y in list2]

# my solution
for i in list1:
    for j in list2:
        list3.append(i+j)


print(list3)
print(list4)

# Learned to use list comprehension to shorten code