import os

seeds = []

mappings= []

soil = []  

constWidth= 100

widthExtraInformation = 5

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

#-------------------------------------------------------------------------
#                               Part 2
#-------------------------------------------------------------------------

class Seed:
    parent = None
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

def startInMapRange(seed, mapping):
    return seed.start >= mapping.source and seed.start < mapping.source + mapping.mapRange and seed.start + seed.seedRange <= mapping.source + mapping.mapRange

def seedRangeInMapRange(seed, mapping):
    return seed.start < mapping.source and seed.start + seed.seedRange >= mapping.source and seed.start + seed.seedRange <= mapping.source + mapping.mapRange

def seedRangeOverMapRange(seed, mapping):
    return seed.start < mapping.source and seed.start + seed.seedRange > mapping.source + mapping.mapRange    
        
def getSeedRangeMapRangeOverlap(seed, mapping):
    
    if startInMapRange(seed, mapping):
        if seed.start + seed.seedRange <= mapping.source + mapping.mapRange:
            deltaMappingStartSeedStart = seed.start - mapping.source
            
            return [Seed(mapping.target + deltaMappingStartSeedStart, seed.seedRange)]
        
        else:
            deltaMappingStartSeedStart = seed.start - mapping.source
            deltaSeedStartMappingEnd = mapping.source + mapping.mapRange - seed.start
            #seed.seedRange < mapping.mapRange so new Seeds are needed 
            newStart = mapping.target + deltaMappingStartSeedStart
            
            return [Seed(newStart, deltaSeedStartMappingEnd), 
                    Seed(mapping.source + mapping.mapRange, seed.seedRange - deltaSeedStartMappingEnd)]
    
    if seedRangeInMapRange(seed, mapping):
        deltaSeedStartMappingStart = mapping.source - seed.start
        newRange = seed.seedRange - deltaSeedStartMappingStart
        
        return [Seed(seed.start, deltaSeedStartMappingStart), 
                Seed(mapping.target, newRange) ]
    
    if seedRangeOverMapRange(seed, mapping):
        deltaSeedStartMappingStart = mapping.source - seed.start
        deltaMappingEndSeedEnd = seed.start + seed.seedRange - (mapping.source + mapping.mapRange)
        
        return [Seed(seed.start, deltaSeedStartMappingStart), 
                Seed(mapping.target, mapping.mapRange), 
                Seed(mapping.source + mapping.mapRange, deltaMappingEndSeedEnd)]
    
    return []

def calcMappedRangesRec(seeds, step):
    if step == len(mappings):
        return seeds
       
    newSeeds = []
    for seed in seeds:
        wasExtended = False
        for mapping in mappings[step]:
            mappedSeed = getSeedRangeMapRangeOverlap(seed, mapping)
            if mappedSeed != []:
                newSeeds.extend(mappedSeed)
                wasExtended = True
                break
            
        if wasExtended == False:
            newSeeds.append(seed)
    
    #print(step +1)
    #for seed in newSeeds:
    #    print(str(seed.start) + " " + str(seed.seedRange))
    #print()
    
    return calcMappedRangesRec(newSeeds, step + 1)

def fillString(string, length):
    while len(string) < length:
        string += " "
    return string

def printDivider(length):
    divider = "+"
    for i in range(0, length):
        divider += "-"
    divider += "+"
    for i in range(0, widthExtraInformation):
        divider += "-"
    divider += "+"
    for i in range(0, widthExtraInformation):
        divider += "-"
    divider += "+"
    print(divider)
    
def printPercentage(seed, target):
    if target==None:
        return fillString("  x", widthExtraInformation) + "|"
    percentage = 100 / seed.seedRange * target.seedRange
    if seed.seedRange == target.seedRange:
        percentage = 100 
    percentage = round(percentage, 1)
    percentage = str(percentage) + "%"
    return fillString(percentage, widthExtraInformation) + "|"

def sumRanges(seeds):
    sumRanges = 0
    for seed in seeds:
        sumRanges += seed.seedRange
    return sumRanges

def calcMappedRanges(seeds):
    
    dummyStatisticsSeeed = Seed(0, sumRanges(seeds))
       
    fullyMappedRange = [seeds]
    idx = 1 
    for mappingRange in mappings:
        newSeeds = []
        print("Filter: " + str(idx))
        print()
        print("Status--------source---range-----(filterSource--filterRange--filterTarget)------target---range---")
        printDivider(constWidth - 1)
        for seed in fullyMappedRange[len(fullyMappedRange) - 1]:
            wasExtended = False
            for mapping in mappingRange:
                mappedSeed = getSeedRangeMapRangeOverlap(seed, mapping)
                if mappedSeed != []:
                    for outputSeed in mappedSeed:
                        outputSeed.parent = seed
                        print(fillString(f"|Filtered: {seed.start} {seed.seedRange} --> {mapping.source, mapping.mapRange, mapping.target} --> {outputSeed.start} {outputSeed.seedRange}" , constWidth) 
                              + "|" 
                              + printPercentage(seed, outputSeed)
                              + printPercentage(dummyStatisticsSeeed, outputSeed))
                    newSeeds.extend(mappedSeed)
                    wasExtended = True
                    break
            
            if wasExtended == False:
                newSeeds.append(seed)
                print(fillString(f"|Pass Through: {seed.start} {seed.seedRange} --> {seed.start} {seed.seedRange}" , constWidth) 
                      + "|" 
                      + printPercentage(seed, None)
                      + printPercentage(dummyStatisticsSeeed, seed))
            printDivider(constWidth -1)
        print()        
        fullyMappedRange.append(newSeeds)
        idx += 1
    
    
    #idx = 1
    #for mappedRange in fullyMappedRange:
    #    print(idx)
    #    sumRanges = 0
    #    for seed in mappedRange:
    #        print(str(seed.start) + " " + str(seed.seedRange))
    #        sumRanges += seed.seedRange
    #    idx += 1
    #    print()
    #    print (sumRanges)
    #    print()
    
    
    
    return fullyMappedRange
    
def letsTry():
    mappedRanges = calcMappedRanges(reorgSeeds())
    smallesStart = mappedRanges[len(mappedRanges) - 1][0].start 
    for seed in mappedRanges[len(mappedRanges) - 1]:
        if seed.start < smallesStart:
            smallesStart = seed.start
            
    return smallesStart   
        
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
file_path = os.path.join(dirname, 'input_05-12-23.txt')

def extractSeeds(seedRow):
    working = seedRow.split(" ")
    for j in range(1, len(working)):
        seeds.append(int(working[j]))

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
        idx = 0
        for value in inputs:
            if value == "\n":
                dirtyMappings.append(stripStrings(builder))
                builder = []
            else:
                builder.append(value)
            if idx == len(inputs) - 1:
                dirtyMappings.append(stripStrings(builder))
            idx += 1
        return cleanMappings(dirtyMappings)
    
    mappings = parseInput()
    
    print ("Part 1: " + str(getLowestSoilIndex()))
    
    print ("Part 2: " + str(letsTry()))
    print ("Part 2(rec): " + str(calcLowestSeed()))