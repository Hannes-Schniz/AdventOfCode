
file_path = "input_01-12-23.txt"
result = 0

# Part One

with open(file_path, "r") as file:
    line = file.readline()
    while line:
        firstValue = 0
        secondValue = 0
        for c in line:
            if c.isnumeric() and firstValue == 0:
                firstValue += int(c)
            if c.isnumeric():
                secondValue = int(c)
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

def getNumber():
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
    return -1

with open(file_path, "r") as file:
    line = file.readline()
    while line:
        firstValue = -1
        secondValue = 0
        idx = 0
        for c in line:
            number = getNumber()
            if number > -1:
                secondValue = number
                if firstValue == -1:
                    firstValue = secondValue
            idx = idx + 1
        result += firstValue * 10 + secondValue
        line = file.readline()
        
print ("Part Two: " + str(result))



