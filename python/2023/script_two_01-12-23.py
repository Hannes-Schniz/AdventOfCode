import os
dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname, 'input_01-12-23.txt')

arr = []


with open(file_path, "r") as file:
    line = file.readline()
    while(line):
        arr.append(line)
        line = file.readline()

key = 0

for i in range(len(arr)):
    erg = ""
    for string in arr[i]:
        for j in range(0,10):
            if string == str(j):
                erg = erg + string
    if len(erg) == 0:
        continue
    first = erg[0]
    last = erg[len(erg) -1]
    erg = first + last
    key = key + int(erg)


print(key)