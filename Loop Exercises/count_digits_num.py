num = int(input("Please enter a number: "))
count = 0
while num != 0:
    num = num//10
    count += 1

print(count)