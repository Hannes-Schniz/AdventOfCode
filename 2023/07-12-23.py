import os, functools



# Contains: [Card(cards = [x..y], value = x, type = (key, highest card(s) in type))]
# for example: [Card(cards = [2, 2, 2, 2, 2], value = 2, type = ("Five of a Kind", 2))]
# for two pairs: [Card(cards = [2, 2, 3, 3, 4], value = 3, type = ("Two Pairs", [3, 2]))]  
handMap = {"High Card": [], 
           "One Pair": [], 
           "Two Pairs": [], 
           "Three of a Kind": [], 
           "Full House": [], 
           "Four of a Kind": [], 
           "Five of a Kind": []}

handHash = {"High Card": [], 
           "One Pair": [], 
           "Two Pairs": [], 
           "Three of a Kind": [], 
           "Full House": [], 
           "Four of a Kind": [], 
           "Five of a Kind": []}

class Hand:
    def __init__(self, cards, value, type):
        self.cards = cards
        self.value = value
        self.type = type
        

def mapCardValue(value):
    if value == "J":
        return 11
    elif value == "Q":
        return 12
    elif value == "K":
        return 13
    elif value == "A":
        return 14
    elif value == "T":
        return 10
    else:
        return int(value)   

def mapCardValueV2(value):
    if value == "J":
        return 1
    return mapCardValue(value) 

def parseInput(line, mapping):
    parsedhand = Hand([], 0, "")
    splittedLine = line.split()
    for char in splittedLine[0]:
        parsedhand.cards.append(mapping(char))
    parsedhand.value = int(splittedLine[1].strip())
    return parsedhand

def isThree(cards):
    sortedCards = sorted(cards)
    for card in sortedCards:
        if sortedCards.count(card) == 3:
            return True
    return False
    
def getHandKey(hand):
    uniqueCards = set(hand.cards)
    if len(uniqueCards) == 1:
        return "Five of a Kind"
    if len(uniqueCards) == 2:
        if isThree(hand.cards):
            return "Full House"
        return "Four of a Kind"
    if len(uniqueCards) == 3:
        if isThree(hand.cards):
            return "Three of a Kind"
        return "Two Pairs"
    if len(uniqueCards) == 4:
        return "One Pair"
    return "High Card"

def sortStrength(hashMap):
    sortedHands = []
    for key in hashMap.keys():
        currHands = hashMap[key].copy()
        if len(currHands) == 0:
            continue
        sortedHands.extend(sorted(currHands, key=lambda hand: hand.cards))
    return sortedHands

#-------------------------------------------------------------------------
#                               Part 1
#-------------------------------------------------------------------------

def calcResult(hands):
    result= 0
    idx = 1
    for hand in hands:
        result += hand.value * idx
        idx += 1
    return result

def mapHand(hand):
    handType = getHandKey(hand)
    hand.type = handType
    handMap[handType].append(hand)

#-------------------------------------------------------------------------
#                               Part 2
#-------------------------------------------------------------------------

def mostCommonCard(hand):
    sortedCards = sorted(hand.cards)
    mostCommonNumber = 0
    for card in sortedCards:
        if card == 1:
            continue
        if sortedCards.count(card) > sortedCards.count(mostCommonNumber) or (sortedCards.count(card) == sortedCards.count(mostCommonNumber) and card > mostCommonNumber):
            mostCommonNumber = card
            
    return mostCommonNumber

def replaceJokerWithMostCommonNumber(hand):
    newHand = Hand(hand.cards.copy(), hand.value, hand.type)
    newValue = mostCommonCard(hand)
    for i in range(len(hand.cards)):
        if newHand.cards[i] == 1:
            newHand.cards[i] = newValue
    return newHand      
        
def mapHandV2(hand):
    handType = getHandKey(replaceJokerWithMostCommonNumber(hand))
    hand.type = handType
    handHash[handType].append(hand)        
    
#-------------------------------------------------------------------------
#                                General
#-------------------------------------------------------------------------

dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname, 'input_07-12-23.txt')

with open(file_path, "r") as file:
    
    input = file.readline()
    while input:
        mapHand(parseInput(input, mapCardValue))
        mapHandV2(parseInput(input, mapCardValueV2))
        input = file.readline()

    
print("Part 1: " + str(calcResult(sortStrength(handMap))))

print("Part 2: " + str(calcResult(sortStrength(handHash))))
    