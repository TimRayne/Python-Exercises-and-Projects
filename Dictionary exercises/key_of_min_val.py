sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

smallest = 0


for i in sample_dict:
    val = sample_dict.get(i)
    if smallest == 0:
        smallest = val
    if smallest > val:
        smallest = val
        key = i

print(key)