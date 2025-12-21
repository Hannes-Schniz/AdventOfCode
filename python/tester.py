import importlib
import math
import pathlib
import re
import time
from os import listdir
from os.path import isdir, isfile, join


def getInput(max):
    userInput = input()
    if userInput == "q":
        exit(0)
    try:
        userInput = int(userInput)
        if userInput >= max:
            print("Please enter a valid input")
            return getInput(max)
    except:
        print("Please enter a valid input")
        return getInput(max)
    return userInput


BASE_PATH = pathlib.Path(__file__).parent.resolve()


print("Welcome to the AdventOfCode Pyhton testing tool")


def getYear(BASE_PATH):
    REGEX = "2.*"

    years = [
        d
        for d in listdir(BASE_PATH)
        if isdir(join(BASE_PATH, d)) and re.search(REGEX, join(BASE_PATH, d))
    ]

    print("Please choose a year:")

    print("+-" + "-" * len(years[0]) + "-+-" + "-----+")
    i = 0
    for year in years:
        print("| " + year + " | " + " " * (4 - len(str(i))) + str(i) + " |")
        i += 1
    print("+-" + "-" * len(years[0]) + "-+-" + "-----+")

    return years[getInput(i)]


def getScript(selectedYear, BASE_PATH):
    PATH_SCRIPTS = str(BASE_PATH) + "/" + selectedYear
    PATH_INPUT = str(BASE_PATH) + "/" + selectedYear + "/input/"
    PATH_TESTS = str(BASE_PATH) + "/" + selectedYear + "/tests"
    REGEX = "script.*"
    scripts = sorted(
        [
            f
            for f in listdir(PATH_SCRIPTS)
            if isfile(join(PATH_SCRIPTS, f)) and re.search(REGEX, join(PATH_SCRIPTS, f))
        ]
    )
    print("Choose a script to test the input on:")

    print("+-" + "-" * len(scripts[0]) + "-+-" + "-----+------+")
    print("|      scripts         | real | test |")
    print("+-" + "-" * len(scripts[0]) + "-+-" + "-----+------+")
    i = 0
    for script in scripts:
        print(
            "| "
            + script
            + " | "
            + " " * (4 - len(str(i)))
            + str(i)
            + " | "
            + " " * (4 - len(str(i + 1)))
            + str(i + 1)
            + " |"
        )
        i += 2
    print("+-" + "-" * len(scripts[0]) + "-+-" + "-----+------+")

    choice = getInput(i)

    selectedScript = scripts[math.floor(choice / 2)]

    PATH_SELECTED_INPUT = ""
    if choice % 2 == 0:
        PATH_SELECTED_INPUT = PATH_INPUT
    else:
        PATH_SELECTED_INPUT = PATH_TESTS

    module = importlib.import_module(selectedYear + "." + selectedScript.split(".")[0])
    my_class = getattr(module, "main")()

    return (selectedScript, PATH_SELECTED_INPUT, my_class)


# exec("import " + PATH_SCRIPTS + "/" +  userChoice.split(".")[0] + " as script")

selectScript = getScript(getYear(BASE_PATH), BASE_PATH)


def loadInput(inputPath, script):
    arr = []
    full_path = inputPath + "/" + script.split(".")[0].split("_")[0] + "_input.txt"
    print(full_path)
    with open(full_path, "r") as file:
        line = file.readline()
        while line:
            arr.append(line)
            line = file.readline()
    return arr


key = 0

start = time.time()
solution = selectScript[2].solutionOne(loadInput(selectScript[1], selectScript[0]))
end = time.time()
print(f"{solution}\r")
print(f"Runtime (s) -> {round(end - start, 10)}")

start = time.time()
print(selectScript[2].solutionTwo(loadInput(selectScript[1], selectScript[0])))
end = time.time()
print(f"Runtime (s) -> {round(end - start, 10)}")
