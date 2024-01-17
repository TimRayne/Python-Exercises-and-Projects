def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        print("Yes,", num, "is a palindrome")
    else: 
        print("No", num, "is not a palindrome")

is_palindrome(121)