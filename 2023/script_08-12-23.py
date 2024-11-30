import os

start = 0

directions = []

tree = {}

def parseInput(line):
    if(line == "\n"):
        return
    splittedLine = line.split(" = ")
    splittedLine[1] = splittedLine[1].strip()
    splittedLine[1] = splittedLine[1][1:-1].split(", ")
    tree[splittedLine[0]] = splittedLine[1]
    

#-------------------------------------------------------------------------
#                               Part 1
#-------------------------------------------------------------------------

def traverse():
    currPos = start
    count = 0
    while currPos != "ZZZ":
        for direction in directions:
            if direction == 0:
                currPos = tree[currPos][0]
            elif direction == 1:
                currPos = tree[currPos][1]
            count += 1
    return count
        
#-------------------------------------------------------------------------
#                               Part 2
#-------------------------------------------------------------------------

      
    
#-------------------------------------------------------------------------
#                                General
#-------------------------------------------------------------------------

dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname, 'input_08-12-23.txt')

with open(file_path, "r") as file:
    
    input = file.readline()
    for char in input[0:-1]:
        translated = 0
        if char == "L":
            translated = 0
        else:
            translated = 1
        directions.append(translated)
    input = file.readline()
    input = file.readline()
    start = input.split(" ")[0]
    while input:
        parseInput(input)
        input = file.readline()

traverse()

#x > 10530 11567
print("Part 1: " + str(traverse()))

#print("Part 2: " + str(calcResult(sortStrength(handHash))))
    