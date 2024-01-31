str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
res_list = []

for i in str_list:
    if i:
        res_list.append(i)
    else:
        continue

print(res_list)