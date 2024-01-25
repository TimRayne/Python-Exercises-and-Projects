str1 = 'PyNaTive'

print("Original String is:", str1)

upper = []
lower = []

for i in str1:
    if i.isupper():
        upper.append(i)
    else:
        lower.append(i)

sorted_str = ''.join(lower + upper)
print('Result is:', sorted_str)