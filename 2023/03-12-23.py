import os
dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname, 'input_03-12-23.txt')

def getNumber(line, idx):
    result = ""
    numberIDX = idx

    #get start of the number
    while line[numberIDX].isnumeric() == True:
        numberIDX -=1
        if numberIDX <= 0:
            break
    numberIDX += 1
    while line[numberIDX].isnumeric() == True:
        result += line[numberIDX]
        numberIDX += 1
        if numberIDX >= len(line):
            break
    return int(result)
    


def analyseSurround(lines, idx):
    # [., ., .] -1/-1 0/-1 1/-1
    # [., x, .] -1/0 0/0 1/0
    # [., ., .] -1/1 0/1 1/1
    
    results =[]
    
    startIDX = idx - 1
    endIDX = idx + 1
    
    if startIDX < 0:
        startIDX = 0
    if endIDX >= len(lines[1]):
        endIDX = len(lines[1]) -1
        
    # print(lines[0][startIDX], lines[0][idx], lines[0][endIDX])
    # print(lines[1][startIDX], lines[1][idx], lines[1][endIDX])
    # print(lines[2][startIDX], lines[2][idx], lines[2][endIDX])
    # print()
    
        
    
    for line in lines:
        if line == "":
                continue
        for i in range(startIDX, endIDX +1):
            if line[i].isnumeric():
                number = getNumber(line, i)
                if results.__contains__(number) == False:
                    results.append(number)
        
    return results
idx = 0
lines = ["", "", ""]
results = []

with open(file_path, "r") as file:
    while idx < 3:
        # gets previous, curr and next line
        if idx != 0:
            lines[1]= lines[2]
        lines[2] = file.readline()
        
        # gets the special char
        currPos = 0
        for c in lines[1]:
            if c.isnumeric() == False and c != '.' and c != "\n":
                results.append(analyseSurround(lines, currPos)) 
            currPos += 1
        
        lines[0] = lines[1]
        idx += 1
    print(results)