import os
    

class Race:
    def __init__(self, time, distance):
        self.time = time
        self.distance = distance



#-------------------------------------------------------------------------
#                               Part 1
#-------------------------------------------------------------------------
             

def calcDistance(time, speed):
    return time * speed  
    


# 1 sec => (7s-1s) * 1 = 6
# 2 sec => (7s-2s) * 2 = 10
# (totalTime - timeCharged) * timeCharged = distance
# 
def findWinningTimes(race):
    winnings = 0
    for i in range(1, race.time ):
        distance = calcDistance(race.time - i, i)
        if distance > race.distance:
            winnings +=1
        percentage = str(100/race.time * (race.time - i))
        print("Calulations left: " + percentage[:4] + "%", end='\r')
    return winnings
    

def calcResult(races):
    sumWinnings = 1
    for race in races:
        sumWinnings = findWinningTimes(race) * sumWinnings
    return sumWinnings  


#-------------------------------------------------------------------------
#                               Part 2
#-------------------------------------------------------------------------


def mergeNumbers(races):

    mergedTime = ""
    mergedDistance = ""
    for race in races:
        mergedTime += str(race.time)
        mergedDistance += str(race.distance)
    return Race(int(mergedTime), int(mergedDistance))
    
        

#-------------------------------------------------------------------------
#                                General
#-------------------------------------------------------------------------

dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname, 'input_06-12-23.txt')



def parseInput(lineOne, lineTwo):
    parsedInput = []
    valuesTime = list(filter(None, lineOne.split(":")[1].strip().split(" ")))
    valuesDist = list(filter(None, lineTwo.split(":")[1].strip().split(" ")) )  
    for i in range(len(valuesTime)):
        parsedInput.append(Race(int(valuesTime[i]), int(valuesDist[i])))
    return parsedInput
    
    




with open(file_path, "r") as file:
    parsedInput = parseInput(file.readline(), file.readline())
    print("Part 1: " + str(calcResult(parsedInput))  + "           ")
    print("Part 2: " + str(findWinningTimes(mergeNumbers(parsedInput))))
    