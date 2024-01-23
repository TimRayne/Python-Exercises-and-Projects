def generate_list():
    nums = list()
    for i in range(4, 30):
        if i % 2 == 0:
            nums.append(i)
    print(nums)

generate_list()