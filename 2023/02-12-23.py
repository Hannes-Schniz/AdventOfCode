import os
dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname, 'input_02-12-23.txt')

# Part One

maxRed = 12
maxGreen = 13
maxBlue = 14
game = 1

colors = [["red", maxRed], ["green", maxGreen], ["blue", maxBlue]]

def splitDraw(draws):
    elements = []
    for draw in draws:
        strippedDraw = draw.strip()
        elements.append(strippedDraw.split(" "))       
    return elements

def checkColors(colorDoubles):
    for color in colors:
        if color[0] == colorDoubles[1] and color[1] >= int(colorDoubles[0]):
            return True
    return False
    
    
def checkDraws(parsedDraws):
    for draw in parsedDraws:
        if (checkColors(draw) == False):
            return False
    return True

with open(file_path, "r") as file:
    result = 0
    line = file.readline()
    while line:
        values = line.split(":")
        runs = values[1].split(";")
        runResults = []
        for run in runs:

            draws = run.split(",")
            parsedDraws = splitDraw(draws)
            runResults.append(checkDraws(parsedDraws))
        if runResults.__contains__(False):
            game += 1
            line = file.readline()
            continue
        result += game            
        game += 1
        line = file.readline()
    print("Part One: " + str(result))
    
# Part Two

game = 1

def getMinColors(colorDoubles, minDraws):
    idx = 0
    for color in colors:
        if color[0] == colorDoubles[1]:
            if minDraws[idx] == 0:
                minDraws[idx] = int(colorDoubles[0])
            elif int(colorDoubles[0]) > minDraws[idx]:
                minDraws[idx] = int(colorDoubles[0])
        idx += 1
    return minDraws

def minDraws(parsedDraws):
    # 0 = red, 1 = green, 2 = blue
    minDraws = [0,0,0]
    for draw in parsedDraws:
        minDraws = getMinColors(draw, minDraws)
    return minDraws

def compareRuns(runResults):
    minResults = [runResults[0][0], runResults[0][1], runResults[0][2]]
    for run in runResults:
        for i in range(0,3):
            if (minResults[i] == 0):
                minResults[i] = int(run[i])
            elif int(minResults[i]) < int(run[i]) and int(run[i]) != 0:
                minResults[i] = int(run[i])
    return minResults

def calcResults(minResults):
    result = 1
    for i in range(0,3):
        result = int(minResults[i]) * result
    return result

with open(file_path, "r") as file:
    result = 0
    line = file.readline()
    while line:
        values = line.split(":")
        runs = values[1].split(";")
        runResults = []
        for run in runs:
            draws = run.split(",")
            parsedDraws = splitDraw(draws)
            runResults.append(minDraws(parsedDraws))
        print (compareRuns(runResults))  
        result += calcResults(compareRuns(runResults))          
        game += 1
        line = file.readline()
    print("Part Two: " + str(result))
