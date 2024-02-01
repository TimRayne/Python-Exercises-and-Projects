str1 = "Emma25 is Data scientist50 and AI Expert"
print("The original string is : " + str1)

lst = []

strList = str1.split()

for i in strList:
    if any(char.isalpha() for char in i) and any(char.isdigit() for char in i):
        lst.append(i)


print("")
print('Appended list is: ')
for i in lst:
    print(i)