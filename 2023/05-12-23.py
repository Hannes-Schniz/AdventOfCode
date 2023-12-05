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

def rangesOverlap(seed, mapping):
    if seed.start >= mapping.source and seed.start < mapping.source + mapping.mapRange:
        return True
    if seed.start + seed.seedRange > mapping.source and seed.start + seed.seedRange <= mapping.source + mapping.mapRange:
        return True
    return False

def startInMapRange(seed, mapping):
    return seed.start >= mapping.source and seed.start < mapping.source + mapping.mapRange and seed.start + seed.seedRange <= mapping.source + mapping.mapRange

def seedRangeInMapRange(seed, mapping):
    return seed.start < mapping.source and seed.start + seed.seedRange >= mapping.source 

def seedRangeOverMapRange(seed, mapping):
    return seed.start < mapping.source and seed.start + seed.seedRange > mapping.source + mapping.mapRange    
        
def getSeedRangeMapRangeOverlap(seed, mapping):
    newSeeds = [seed]
    
    if startInMapRange(seed, mapping):
        if seed.start + seed.seedRange <= mapping.source + mapping.mapRange:
            deltaMappingStartSeedStart = seed.start - mapping.source
            newSeeds = [Seed(mapping.target + deltaMappingStartSeedStart, seed.seedRange)]
        else:
            deltaMappingStartSeedStart = seed.start - mapping.source
            #seed.seedRange < mapping.mapRange so new Seeds are needed 
            newRange = mapping.mapRange - deltaMappingStartSeedStart
            newStart = mapping.target + deltaMappingStartSeedStart
            newSeeds = [Seed(newStart, newRange), Seed(seed.start + newRange, seed.seedRange - newRange)]
    
    if seedRangeInMapRange(seed, mapping):
        deltaSeedStartMappingStart = mapping.source - seed.start
        newRange = seed.seedRange - deltaSeedStartMappingStart
        newSeeds = [Seed(seed.start, deltaSeedStartMappingStart), Seed(mapping.target, seed.seedRange - deltaSeedStartMappingStart) ]
    
    if seedRangeOverMapRange(seed, mapping):
        deltaSeedStartMappingStart = mapping.source - seed.start
        deltaMappingEndSeedEnd = seed.start + seed.seedRange - (mapping.source + mapping.mapRange)
        newSeeds = [Seed(seed.start, deltaSeedStartMappingStart), Seed(mapping.target, mapping.mapRange), Seed(mapping.source + mapping.mapRange, deltaMappingEndSeedEnd)]
    return newSeeds

def calcMappedRangesRec(seeds, step):
    if step == len(mappings):
        return seeds
    
    #for seed in seeds:
    #    
    #    for mapping in mappings[step]:
    #        newSeeds = []
    #        newSeeds.extend(getSeedRangeMapRangeOverlap(seed, mapping))
            
        
    for mapping in mappings[step]:
        newSeeds = []
        for seed in seeds:
            newSeeds.extend(getSeedRangeMapRangeOverlap(seed, mapping))
    for seed in newSeeds:
        print(str(seed.start) + " " + str(seed.seedRange))
    print()
    return calcMappedRangesRec(newSeeds, step + 1)
        
def calcLowestSeed():
    mappedRanges = calcMappedRangesRec(reorgSeeds(), 0)
    smallesStart = mappedRanges[0].start
    for mappedRange in mappedRanges:
        if mappedRange.start < smallesStart:
            smallesStart = mappedRange.start
    return smallesStart
    
#-------------------------------------------------------------------------
#                                General
#-------------------------------------------------------------------------

dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname, 'input_05-12-23-test.txt')

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
    print ("Part 2: " + str(calcLowestSeed()))