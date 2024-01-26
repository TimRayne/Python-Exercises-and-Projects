str1 = "Welcome to USA. usa awesome, isn't it?"
x = 0
count = 0
str1 = str1.lower()
for i in str1:
    index = str1[x:x + 3]
    if index == "usa":
        count += 1
    x += 1

print("USA Appears", count, "times")

# Could also use count() function