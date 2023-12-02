import os
dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname, 'input_02-12-23.txt')

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
        print("Game: " + str(game))
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
        print(result)
        line = file.readline()
    print(result)