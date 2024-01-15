def incometax(income):
    if income > 20000:
        over20k = income-20000
        over_20k_tax = over20k*.2
        totaltax = over_20k_tax + 1000
        print(totaltax)
    elif income <= 20000:
        totaltax = income * .1
        print(totaltax)
    else:
        print(income)
    
incometax(15000)