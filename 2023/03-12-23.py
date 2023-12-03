import os
dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname, 'input_03-12-23.txt')

results = []

# results= []
# length = 104
# while length > 0:
#     results.append([])
#     length -= 1


class Key:
    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.x = x
        self.y = y
    def eql(self, input):
        if self.symbol == input.symbol and self.x == input.x and self.y == input.y:
            return True

def checkIfContains(input):
    for result in results:
        if result.eql(input):
            return True
    return False

#gets the full number and returns the number as a unique object
def getNumber(line, idx, currLine):
    result = ""

    #get start of the number
    while line[idx].isnumeric() == True:
        idx -=1
    idx += 1
    start = idx
    
    #builds the number
    while line[idx].isnumeric() == True:
        result += line[idx]
        idx += 1
        if idx >= len(line):
            break
        
    return Key(int(result), start, currLine)
    

#draws a box around the target symbol and searches for digits
def analyseSurround(lines, idx, currLine):
    # [., ., .] -1/-1 0/-1 1/-1
    # [., x, .] -1/0 0/0 1/0
    # [., ., .] -1/1 0/1 1/1
    
    
    # gets the top left and bottom right corner of the 3x3 square
    startIDX = idx - 1
    endIDX = idx + 1
    
    if startIDX < 0:
        startIDX = 0
    if endIDX >= len(lines[1]):
        endIDX = len(lines[1]) - 1
        
    # print(lines[0][startIDX], lines[0][idx], lines[0][endIDX])
    # print(lines[1][startIDX], lines[1][idx], lines[1][endIDX])
    # print(lines[2][startIDX], lines[2][idx], lines[2][endIDX])
    # print()
    
    #current line relative to the symbol line
    lineDelta = -1
    
    for line in lines:
        for i in range(startIDX, endIDX + 1):
            if line[i].isnumeric():
                number = getNumber(line, i, (currLine + lineDelta))
                if checkIfContains(number) == False:
                    results.append(number)                
        lineDelta += 1

def sumResults():
    calcResult = 0
    for result in results:
        calcResult += result.symbol
    return calcResult
 


with open(file_path, "r") as file:
    idx = 0
    lines = ["", "", ""]
    
    while idx < 141:
        # gets previous, curr and next line
        if idx != 0:
            lines[1]= lines[2]
        lines[2] = file.readline()
        
        #Current x value
        currPos = 0
        
        # gets the special char
        for c in lines[1]:
            if c.isnumeric() == False and c != '.' and c != "\n":
                analyseSurround(lines, currPos, idx)
            currPos += 1
        
        lines[0] = lines[1]
        idx += 1
    print("Part 1: " + str(sumResults()))