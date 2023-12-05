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


        
        
        

#-------------------------------------------------------------------------
#                                General
#-------------------------------------------------------------------------

dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname, 'input_05-12-23-test.txt')



def stripStrings(strings):
    return [string.rstrip() for string in strings]

def cleanMappings(dirtyMappings):
    cleanMappings = []
    for i in range(0, len(dirtyMappings)):
        if i == 0:
            working = dirtyMappings[i][0].split(" ")
            for j in range(1, len(working)):
                seeds.append(int(working[j]))
            continue
        
        #print(dirtyMappings[i][0][0])
        workingMapping = []
        for value in dirtyMappings[i]:
            if value[0][0].isnumeric() == False:
                continue
            value = value.split(" ")
            workingMapping.append( Mapping(int(value[0]), int(value[1]), int(value[2])))
            #print(cleanMappings[-1].source, cleanMappings[-1].target, cleanMappings[-1].mapRange)
        cleanMappings.append(workingMapping)
    return cleanMappings


def checkIfInMapRange(mapping, value):
    if value >= mapping.source and value <= mapping.source + mapping.mapRange - 1:
        return True
    return False

def getSoilIndex(targetIdx):
    for mapping in mappings[0]:
        if checkIfInMapRange(mapping, targetIdx):
            return mapping.target + targetIdx - mapping.source
    return targetIdx    


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
    print (getSoilIndex(100))