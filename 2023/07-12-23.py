import os



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

def deMapCardValue(value):
    if value == 10:
        return "T"
    elif value == 11:
        return "J"
    elif value == 12:
        return "Q"
    elif value == 13:
        return "K"
    elif value == 14:
        return "A"
    else:
        return str(value) 

def sortCards(cards):
    return sorted(cards, reverse=True)



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



#-------------------------------------------------------------------------
#                               Part 2
#-------------------------------------------------------------------------


  

#-------------------------------------------------------------------------
#                                General
#-------------------------------------------------------------------------

dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname, 'input_07-12-23.txt')



def parseInput(line):
    parsedCards = []
    parsedhand = Hand([], 0, "")
    
    splittedLine = line.split(" ")
    for char in splittedLine[0]:
        parsedCards.append(mapCardValue(char))
    parsedhand.cards = parsedCards
    
    parsedhand.value = int(splittedLine[1].strip())
    
    
    return parsedhand
    
def matchCards(hand):
    cardsMap = {}
    for card in hand.cards:
        if card in cardsMap:
            cardsMap[card] += 1
        else:
            cardsMap[card] = 1
    return cardsMap

def checkFullHouse(cardsMap):
    if 2 in cardsMap.values():
        return True
    return False

def checkTwoPair(cardsMap):
    pairs = []
    for card in cardsMap:
        if cardsMap[card] == 2:
            pairs.append(card)
    if len(pairs) == 2:
        return (True, sortCards(pairs))
    return False

def getHandKey(hand):
    cardsMap = matchCards(hand)
    for card in cardsMap:
        if cardsMap[card] == 5:
            return ("Five of a Kind", [card])
        elif cardsMap[card] == 4:
            return ("Four of a Kind", [card])
        elif cardsMap[card] == 3:
            if checkFullHouse(cardsMap):
                return ("Full House", [card])
            return ("Three of a Kind", [card])
        elif cardsMap[card] == 2:
            isTwoPair = checkTwoPair(cardsMap)
            if isTwoPair:
                return ("Two Pairs", isTwoPair[1])
            return ("One Pair", [card])
    return ("High Card", [sortCards(hand.cards)[0]])

    
def mapHand(hand):
    handType = getHandKey(hand)
    hand.type = handType
    handMap[handType[0]].append(hand)
    
#returns -1 if cardsOne < cardsTwo, 1 if > and 0 if =
def compareCards(cardsOne, cardsTwo):
    for i in range(0,len(cardsOne)):
        if cardsTwo[i] == cardsOne[i]:
            continue
        if cardsOne[i] < cardsTwo[i]:
            return -1
        elif cardsOne[i] > cardsTwo[i]:
            return 1
    return 0

def getWeakest(hands):
    weakest = hands[0]
    #gets the hand with the highest numbers in the type
    for i in range(0,len(hands)):
                
        comparedResult = compareCards(weakest.cards, hands[i].cards)
        if comparedResult == 1:
            weakest = hands[i]
            
           
    return weakest

def sortStrength():
    sortedHands = []
    for key in handMap.keys():
        currHands = handMap[key].copy()
        if len(currHands) == 0:
            continue
        while len(currHands) > 0:
            weakestHand = getWeakest(currHands)
            sortedHands.append(weakestHand)
            currHands.remove(weakestHand)   
    return sortedHands

with open(file_path, "r") as file:
    
    #TODO: Parse input
    input = file.readline()
    while input:
        mapHand(parseInput(input))
        input = file.readline()
    
    sortedHands = sortStrength()
    
    print("Part 1: " + str(calcResult(sortedHands))  + "           ")
    #print("Part 2: " + str(findWinningTimes(mergeNumbers(parsedInput))))
    