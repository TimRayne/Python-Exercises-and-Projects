sample_dict = {'a': 100, 'b': 200, 'c': 300}

for i in sample_dict:
    if sample_dict.get(i) == 200:
        print('200 is present in sample dict')