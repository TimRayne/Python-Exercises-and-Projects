# print(max(nums)) would also work

nums = [4, 6, 8, 24, 12, 2]
largest = 0
for i in nums:
    if i > largest:
        largest = i
    
print(largest)
