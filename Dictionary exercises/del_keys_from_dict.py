sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

for i in keys:
    if i in sample_dict:
        del sample_dict[i]

print(sample_dict)