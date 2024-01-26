s1 = "Yns"
s2 = "PYnative"

def bal_check(s1, s2):
    x = True
    for char in s1:
        if char in s2:
            continue
        else:
            x = False
    return x

print(bal_check(s1, s2))