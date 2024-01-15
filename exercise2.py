def printSum (num):
    for currentnum in range(num):
        previousnum = 0
        if currentnum == 0:
            previousnum == 0
        else: previousnum = currentnum - 1
        sum = currentnum + previousnum
        print("num is", currentnum, "previous num is", previousnum, "Sum is", sum)

printSum(10)
