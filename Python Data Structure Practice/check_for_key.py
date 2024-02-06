roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
new_list = []
pos = 0

for i in sample_dict:
    key = sample_dict.get(i)
    new_list.append(key)

print(new_list)

        