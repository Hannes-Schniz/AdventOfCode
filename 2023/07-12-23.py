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



#-------------------------------------------------------------------------
#                               Part 1
#-------------------------------------------------------------------------
             
# idea:
# parse input into Hand Objet 
# Map Hand Objects to a Hashmap containing  all types of Hands
# Sort every list of Hands in the Hashmap from best to worst
# merge all lists into one list
# calculate Winnings



#-------------------------------------------------------------------------
#                               Part 2
#-------------------------------------------------------------------------


  

#-------------------------------------------------------------------------
#                                General
#-------------------------------------------------------------------------

dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname, 'input_07-12-23-test.txt')



def parseInput(line):
    parsedCards = []
    parsedhand = Hand([], 0, "")
    
    splittedLine = line.split(" ")
    for char in splittedLine[0]:
        parsedCards.append(mapCardValue(char))
    parsedhand.cards = parsedCards
    
    parsedhand.value = int(splittedLine[1].strip())
    
    return parsedhand
 
def sortCards(cards):
    return sorted(cards, reverse=True)
    
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
            return ("Five of a Kind", card)
        elif cardsMap[card] == 4:
            return ("Four of a Kind", card)
        elif cardsMap[card] == 3:
            if checkFullHouse(cardsMap):
                return ("Full House", card)
            return ("Three of a Kind", card)
        elif cardsMap[card] == 2:
            isTwoPair = checkTwoPair(cardsMap)
            if isTwoPair:
                return ("Two Pairs", isTwoPair[1])
            return ("One Pair", card)
    return ("High Card", sortCards(hand.cards)[0])

    
def mapHand(hand):
    handType = getHandKey(hand)
    hand.type = handType
    handMap[handType[0]].append(hand)

def sortStrength(hands):
    print("TODO")
    
    



with open(file_path, "r") as file:
    
    #TODO: Parse input
    input = file.readline()
    while input:
        mapHand(parseInput(input))
        input = file.readline()
    print("TODO")
    #print("Part 1: " + str(calcResult(parsedInput))  + "           ")
    #print("Part 2: " + str(findWinningTimes(mergeNumbers(parsedInput))))
    