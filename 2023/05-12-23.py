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
        for value in dirtyMappings[i]:
            if value[0][0].isnumeric() == False:
                continue
            value = value.split(" ")
            cleanMappings.append( Mapping(int(value[0]), int(value[1]), int(value[2])))
            #print(cleanMappings[-1].source, cleanMappings[-1].target, cleanMappings[-1].mapRange)
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
    print(seeds)

    



    