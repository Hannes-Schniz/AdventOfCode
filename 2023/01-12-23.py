import os
dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname, 'input_01-12-23.txt')

result = 0

NaN = -1

# Part One

with open(file_path, "r") as file:
    line = file.readline()
    while line:
        firstValue = NaN
        secondValue = 0
        for c in line:
            if c.isnumeric():
                secondValue = int(c)
                if firstValue == NaN:
                    firstValue = secondValue
        result += firstValue * 10 + secondValue
        line = file.readline()        

print("Part One: " + str(result))
    
# Part Two

result = 0

spelledNumersAsKeys = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4, 
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0
}

def isNumber(input):
    if spelledNumersAsKeys.keys().__contains__(input):
        return True
    return False

def getNumber(c, idx):
    fourLetters = line[idx:idx+4:1]
    threeLetters = line[idx:idx+3:1]
    fiveLetters = line[idx:idx+5:1]
    if c.isnumeric():
        return int(c)
    if isNumber(threeLetters):
        return spelledNumersAsKeys[threeLetters]
    if isNumber(fourLetters):
        return spelledNumersAsKeys[fourLetters]
    if isNumber(fiveLetters):
        return spelledNumersAsKeys[fiveLetters]
    return NaN

def checkLine():
    firstValue = NaN
    secondValue = 0
    idx = 0
    for c in line:
        number = getNumber(c, idx)
        if number == NaN:
            idx = idx + 1
            continue
        secondValue = number
        if firstValue == NaN:
            firstValue = secondValue
        idx = idx + 1
    return firstValue, secondValue
    

with open(file_path, "r") as file:
    line = file.readline()
    while line:
        values = checkLine()
        result += values[0] * 10 + values[1]
        line = file.readline()
        
print ("Part Two: " + str(result))