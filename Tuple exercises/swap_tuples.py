tuple1 = (11, 22)
tuple2 = (99, 88)

#new lists
list1 = []
list2 = []

#append lists with numbers
for i in tuple1:
    list2.append(i)
for i in tuple2:
    list1.append(i)

tuple1 = tuple(list1)
tuple2 = tuple(list2)

print('Tuple1:', tuple1)
print('Tuple2:', tuple2)