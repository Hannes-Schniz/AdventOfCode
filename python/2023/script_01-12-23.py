class main:
    import os

    # Part One

    def solutionOne(lines):
        result = 0
        for line in lines:
                firstValue = -1
                secondValue = 0
                for c in line:
                    if c.isnumeric():
                        secondValue = int(c)
                        if firstValue == -1:
                            firstValue = secondValue
                result += firstValue * 10 + secondValue
                
                    

        return(str(result))

    def solutionTwo(lines):
        result = 0

        NaN = -1

        spelledNumersAsKeys = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4, 
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "zero": 0
        }

        def isNumber(input):
            if spelledNumersAsKeys.keys().__contains__(input):
                return True
            return False

        def getNumber(c, idx):
            fourLetters = line[idx:idx+4:1]
            threeLetters = line[idx:idx+3:1]
            fiveLetters = line[idx:idx+5:1]
            if c.isnumeric():
                return int(c)
            if isNumber(threeLetters):
                return spelledNumersAsKeys[threeLetters]
            if isNumber(fourLetters):
                return spelledNumersAsKeys[fourLetters]
            if isNumber(fiveLetters):
                return spelledNumersAsKeys[fiveLetters]
            return NaN

        def checkLine():
            firstValue = NaN
            secondValue = 0
            idx = 0
            for c in line:
                number = getNumber(c, idx)
                if number == NaN:
                    idx = idx + 1
                    continue
                secondValue = number
                if firstValue == NaN:
                    firstValue = secondValue
                idx = idx + 1
            return firstValue, secondValue


        for line in lines:
            values = checkLine()
            result += values[0] * 10 + values[1]
            
        return(str(result))