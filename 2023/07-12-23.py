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
        #list of cards from input
        self.cards = cards
        #value of hand from input
        self.value = value
        #tupel (type, highest card(s) in type)
        self.type = type
    
    def sortByType():
        print("TODO")
        
        

        

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

def parseInput(line):
    parsedCards = []
    parsedCardsV2 = []
    parsedhand = Hand([], 0, "")
    parsedhandV2 = Hand([], 0, "")
    splittedLine = line.split(" ")
    for char in splittedLine[0]:
        parsedCards.append(mapCardValue(char))
        parsedCardsV2.append(mapCardValueV2(char))
    parsedhand.cards = parsedCards
    parsedhand.value = int(splittedLine[1].strip())
    parsedhandV2.cards = parsedCardsV2
    parsedhandV2.value = int(splittedLine[1].strip())
    return (parsedhand, parsedhandV2)
    



#-------------------------------------------------------------------------
#                               Part 1
#-------------------------------------------------------------------------
             
# idea:
# parse input into Hand Objet 
# Map Hand Objects to a Hashmap containing  all types of Hands
# Sort every list of Hands in the Hashmap from best to worst
# merge all lists into one list
# calculate Winnings

# incorrect:   x < 248998691 249343586 249199990  249143986  
# x != 249008195 x != 248757566 x != 248192316 x != 248512881

def calcResult(hands):
    result= 0
    idx = 1
    for hand in hands:
        result += hand.value * idx
        idx += 1
    return result


def isThree(cards):
    sortedCards = sorted(cards)
    for card in sortedCards:
        if sortedCards.count(card) == 3:
            return True
    return False

def getHandKey(hand):
    matches = set(hand.cards)
    if len(matches) == 1:
        return "Five of a Kind"
    if len(matches) == 2:
        if isThree(hand.cards):
            return "Full House"
        return "Four of a Kind"
    if len(matches) == 3:
        if isThree(hand.cards):
            return "Three of a Kind"
        return "Two Pairs"
    if len(matches) == 4:
        return "One Pair"
    return "High Card"

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


def sortStrength(hashMap):
    sortedHands = []
    for key in hashMap.keys():
        currHands = hashMap[key].copy()
        if len(currHands) == 0:
            continue
        sortedHands.extend(sorted(currHands, key=lambda hand: hand.cards))
    return sortedHands

with open(file_path, "r") as file:
    
    input = file.readline()
    while input:
        parsedInput = parseInput(input)
        mapHand(parsedInput[0])
        mapHandV2(parsedInput[1])
        input = file.readline()

    
sortedHands = sortStrength(handMap)
    
print("Part 1: " + str(calcResult(sortedHands))  + "           ")

sortedHands = sortStrength(handHash)

print("Part 2: " + str(calcResult(sortedHands)))
    