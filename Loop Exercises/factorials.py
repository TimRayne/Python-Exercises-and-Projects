num = int(input("Please enter a number: "))
total = 1
for i in range(num, 0, -1):
    total *= i

print(total)