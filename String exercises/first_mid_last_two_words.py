def find_middle(s):
    middle = int(len(s)/2)
    return middle

def first_mid_last(s1, s2):
    print("Original strings are:", "\"" + s1 + "\"", "and",  "\"" + s2 + "\"")
    first = s1[0] + s2[0]
    mid_s1 = s1[find_middle(s1)]
    mid_s2 = s2[find_middle(s2)]
    middle = mid_s1 + mid_s2
    last = s1[-1] + s2[-1]
    return(first + middle + last)

print(first_mid_last("America","Japan"))