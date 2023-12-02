import os
dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname, 'input_02-12-23.txt')

maxRed = 12
maxGreen = 13
maxBlue = 14
game = 1

colors = ["red", "green", "blue"]

def splitDraw(draws):
    elements = []
    for draw in draws:
        strippedDraw = draw.strip()
        elements.append(strippedDraw.split(" "))
    
    print(elements)

with open(file_path, "r") as file:
    line = file.readline()
    
    values = line.split(":")
    runs = values[1].split(";")
    for run in runs:
        
        draws = run.split(",")
        splitDraw(draws)
        print(draws)
    
    game += 1
    line = file.readline()