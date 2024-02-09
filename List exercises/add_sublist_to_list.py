list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

sub_list = ["h", "i", "j"]

pos = list1[2][1][2]

for i in sub_list:
    pos.append(i)

print(list1)
