import os

seeds = []

mappings= []

soil = []  

class Mapping:
    def __init__(self, target, source, mapRange):
        self.target = target
        self.source = source
        self.mapRange = mapRange

#-------------------------------------------------------------------------
#                               Part 1
#-------------------------------------------------------------------------
        


#-------------------------------------------------------------------------
#                               Part 2
#-------------------------------------------------------------------------

class Seed:
    def __init__(self, start, seedRange):
        self.start = start
        self.seedRange = seedRange

def reorgSeeds():
    newSeeds = []
    for i in range(0, len(seeds)):
        if i%2 == 1:
            continue
        newSeeds.append(Seed(seeds[i], seeds[i+1]))
    return newSeeds
        
def getLowestSoilIndexV2():
    seeds = reorgSeeds()
    firstRun = True
    minSoilIndex = 0
    idx = 1
    for seed in seeds:
        for i in range(seed.start, seed.start + seed.seedRange - 1):
            currSoilIndex = getSoilIndex(i, 0)
            if firstRun:
                minSoilIndex = currSoilIndex
                firstRun = False
                continue
            if currSoilIndex < minSoilIndex:
                minSoilIndex = currSoilIndex
            print_progress(idx, i, seed.start + seed.seedRange - 1)
        idx += 1
    return minSoilIndex       
        
def print_progress(seed, current_index, total_range):
    progress = round(total_range -current_index )
    print(f'Seed: {seed} Progress: {progress}')

#-------------------------------------------------------------------------
#                                General
#-------------------------------------------------------------------------

dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname, 'input_05-12-23.txt')

def extractSeeds(seedRow):
    working = seedRow.split(" ")
    for j in range(1, len(working)):
        seeds.append(int(working[j]))

def getLowestSoilIndex():
    firstRun = True
    minSoilIndex = 0
    #print(seeds)
    for seed in seeds:
        currSoilIndex = getSoilIndex(seed, 0)
        if firstRun:
            minSoilIndex = currSoilIndex
            firstRun = False
            continue
        if currSoilIndex < minSoilIndex:
            minSoilIndex = currSoilIndex
    return minSoilIndex


def stripStrings(strings):
    return [string.rstrip() for string in strings]

def cleanMappings(dirtyMappings):
    cleanMappings = []
    for i in range(0, len(dirtyMappings)):
        if i == 0:
            extractSeeds(dirtyMappings[i][0])
            continue
        
        workingMapping = []
        for value in dirtyMappings[i]:
            if value[0][0].isnumeric() == False:
                continue
            value = value.split(" ")
            workingMapping.append( Mapping(int(value[0]), int(value[1]), int(value[2])))
        cleanMappings.append(workingMapping)
    return cleanMappings


def checkIfInMapRange(mapping, value):
    return value >= mapping.source and value < mapping.source + mapping.mapRange

def getSoilIndex(targetIdx, step):
    if step == len(mappings):
        #print(targetIdx)
        return targetIdx
    for mapping in mappings[step]:
        if checkIfInMapRange(mapping, targetIdx):
            nextTarget = mapping.target + targetIdx - mapping.source
            #print("Step " + str(step) + ": " + str(targetIdx) + " --> " + str(nextTarget))
            return getSoilIndex(nextTarget, step + 1)
    return getSoilIndex(targetIdx, step + 1)    


with open(file_path, "r") as file:
    
    def parseInput():
        line = file.readline()
        inputs = []
        dirtyMappings = []
        while line:
            inputs.append(line)
            line = file.readline()
        builder = []
        for value in inputs:
            if value == "\n":
                dirtyMappings.append(stripStrings(builder))
                builder = []
            else:
                builder.append(value)
        return cleanMappings(dirtyMappings)
    
    mappings = parseInput()
    print ("Part 1: " + str(getLowestSoilIndex()))
    print ("Part 2: " + str(getLowestSoilIndexV2()))