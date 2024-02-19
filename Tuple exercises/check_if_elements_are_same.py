tuple1 = (45, 45, 45, 45)
num = tuple1[0]
chk = True

for i in tuple1:
    if i != num:
        chk = False
        break

if chk == True:
    print(True)
else:
    print(False)
