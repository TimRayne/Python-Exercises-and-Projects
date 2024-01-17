with open ('test.txt', 'r') as file:
    text = file.readlines()

counter = -1

with open ('new_file.txt', 'w') as new:
    for i in text:
        counter += 1
        if counter == 4:
            continue
        new.write(i)
        print(i)

new.close()



    