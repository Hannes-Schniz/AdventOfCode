import os

# parse input into scratch and winning numbers
# check for each scratch number if the winning numbers contains it
# add up counter for ech containing number
# calc 2^counter
# add up all results

#-------------------------------------------------------------------------
#                               Part 1
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#                               Part 2
#-------------------------------------------------------------------------



#-------------------------------------------------------------------------
#                                General
#-------------------------------------------------------------------------

dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname, 'input_04-12-23-test.txt')

testresult = 13

testRows= [8,2,2,1,0,0]

scratchNumbers = []

winningNumbers = []

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
    
    #TODO fill with code
    line = file.readline()
    parsedInput = parseInput(line)
    scratchNumbers = parsedInput[0]
    winningNumbers = parsedInput[1]
    print(scratchNumbers)
    print(winningNumbers)
    