from os import listdir
from os.path import isfile, join, isdir
import re
import pathlib
import importlib

def getInput():
    userInput = input()
    if userInput == "q":
            exit(0)
    try:
        userInput = int(userInput)
        if userInput >= i:
            print("Please enter a valid input")
            return getInput()
    except:
        print("Please enter a valid input")
        return getInput()
    return userInput


BASE_PATH = pathlib.Path(__file__).parent.resolve()

REGEX = '2.*'

years = [d for d in listdir(BASE_PATH) if isdir(join(BASE_PATH, d))and re.search(REGEX, join(BASE_PATH,d)) ]

print("Welcome to the AdventOfCode Pyhton testing tool")
print("Please choose a year:")

i = 0
for script in years:
    print(str(i)+":", script)
    i += 1

selectedYear = years[getInput()]

PATH_INPUT = str(BASE_PATH) + "/" +  selectedYear + "/input/"
PATH_TESTS = str(BASE_PATH) + "/" +  selectedYear + "/tests"
PATH_SCRIPTS = str(BASE_PATH) + "/"+ selectedYear

REGEX = 'script.*'

tests = [f for f in listdir(PATH_TESTS) if isfile(join(PATH_TESTS, f))]
inputs = [f for f in listdir(PATH_INPUT) if isfile(join(PATH_INPUT, f))]
scripts = [f for f in listdir(PATH_SCRIPTS) if isfile(join(PATH_SCRIPTS, f)) and re.search(REGEX, join(PATH_SCRIPTS, f)) ]


print("Choose a script to test the input on:")

i = 0
for script in scripts:
    print(str(i)+":", script)
    i += 1


    
userChoice = scripts[getInput()]

#exec("import " + PATH_SCRIPTS + "/" +  userChoice.split(".")[0] + " as script")


module = importlib.import_module(selectedYear + "." + userChoice.split(".")[0])
my_class = getattr(module, 'main')


def loadInput(inputPath, script):
    arr = []
    full_path =inputPath + "/input_" + script.split(".")[0].split("_")[1] + ".txt"
    print(full_path)
    with open(full_path, "r") as file:
        line = file.readline()
        while(line):
            arr.append(line)
            line = file.readline()
    return arr

key = 0


print(my_class.solutionOne(loadInput(PATH_INPUT, userChoice)))
print(my_class.solutionTwo(loadInput(PATH_INPUT, userChoice)))
