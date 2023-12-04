import os

# parse input into scratch and winning numbers
# check for each scratch number if the winning numbers contains it
# add up counter for ech containing number
# calc 2^counter
# add up all results

#-------------------------------------------------------------------------
#                               Part 1
#-------------------------------------------------------------------------

testresult = 13

testRows= [8,2,2,1,0,0]

def checkhits(scratchNumbers, winningNumbers):
    count = 0
    for scratchNumber in scratchNumbers:
        if winningNumbers.__contains__(scratchNumber):
            count += 1
    return count

def calcResult(hits):
    if hits == 0:
        return 0
    return 2 ** (hits - 1)
        


#-------------------------------------------------------------------------
#                               Part 2
#-------------------------------------------------------------------------

cards = []



#-------------------------------------------------------------------------
#                                General
#-------------------------------------------------------------------------

dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname, 'input_04-12-23.txt')

class Card():
    def __init__(self, scratchNumbers, winningNumbers):
        self.scratchNumbers = scratchNumbers
        self.winningNumbers = winningNumbers

def parseInput(line):
    parsed = []
    values = line.split(":")
    values = values[1].split("|")
    for value in values:
        value = value.strip()
        numbers = []
        for number in value.split(" "):
            if number != "":
                numbers.append(number)
        parsed.append(numbers)
    return parsed
    




with open(file_path, "r") as file:
    
    runOneResult = 0
    
    runTwoResult = 0
    
    line = file.readline()
    
    idx = 0
    
    doubleLines = []
    
    while line:
        parsedInput = parseInput(line)
        card = Card(parsedInput[0], parsedInput[1])
        hits = checkhits(card.scratchNumbers, card.winningNumbers)
        rowResult = calcResult(hits)
        runOneResult += rowResult
        cards.append(card)
        line = file.readline()
        idx += 1
    print("Part 1: " + str(runOneResult))
    print("Part 2: " + str(runTwoResult))
    