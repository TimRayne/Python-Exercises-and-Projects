import string

s = "/*Jon is @developer & musician"

print("Original string is ", s)

table = str.maketrans(dict.fromkeys(string.punctuation))  # OR {key: None for key in string.punctuation}
new_s = s.translate(table)  

print(new_s)