str1 = "P@#yn26at^&i5ve"

def countStuff(s):
    numCount = 0
    charCount = 0
    symCount = 0
    for i in s:
        if i.isalpha():
            charCount += 1
        elif i.isdigit():
            numCount += 1
        else:
            symCount += 1
    print("The amount of characters is:", charCount)
    print('The amount of numbers is:', numCount)
    print('The amount of symbols is:', symCount)

countStuff(str1)
            