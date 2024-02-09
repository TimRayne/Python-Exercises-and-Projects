sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

new_dict = dict()

for i in keys:
    if i in sample_dict:
        new_dict[i] = sample_dict.get(i)

print(new_dict)