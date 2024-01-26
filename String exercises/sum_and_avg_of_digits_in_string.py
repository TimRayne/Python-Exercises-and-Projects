str1 = "PYnative29@#8496"
res = []
total = 0
numCount = 0

for i in str1:
    if i.isdigit():
        res.append(i)

for i in res:
    total += int(i)
    numCount += 1

avg = total/numCount

print('Sum is:', total, 'Average is:', avg)