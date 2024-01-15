rows = int(input("How many rows would you like?: "))

for i in range(rows+1):
    for j in range(i):
        print(i, end=" ")
    print("\n")