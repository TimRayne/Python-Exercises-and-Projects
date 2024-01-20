n = 5
s = 2
add = 20
total = 0
for i in range(n):
    print("Sequence is at:", s)
    total += s
    s += add
    add *= 10
    print("Total is at:", total)

