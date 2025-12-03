class main:
    def solutionOne(lines):
        lines = [[y for y in x] for x in main.clean_lines(lines)]
        maps = main.split_maps(lines)
        uniques = []
        for key in maps.keys():
            for posOne in maps[key]:
                for posTwo in maps[key]:
                    if posOne == posTwo:
                        continue
                    diff = main.subPositions(posOne,posTwo)
                    diffTwo = main.subPositions(posTwo, diff)
                    diffOne = main.addPositions(posOne, diff)
                    if main.isOnBoard(lines,diffOne):
                        uniques.append((diffOne))
                    if main.isOnBoard(lines,diffTwo):
                        uniques.append((diffTwo))
        #main.printBoard(lines, uniques)
        return len(set(uniques))      

    def solutionTwo(lines):
        lines = [[y for y in x] for x in main.clean_lines(lines)]
        maps = main.split_maps(lines)
        uniques = []
        for key in maps.keys():
            for posOne in maps[key]:
                if len(maps[key]) > 1:
                    uniques.append(posOne)
                for posTwo in maps[key]:
                    if posOne == posTwo:
                        continue
                    diff = main.subPositions(posOne,posTwo)
                    #   print(posOne, posTwo)
                    uniques += main.getAllPositions(lines, posOne, posTwo, diff)   
        #main.printBoard(lines, uniques)       
        return len(set(uniques))
    
    def getAllPositions(lines, posOne, posTwo, diff):
        line = main.findStart(lines, posTwo, diff) +    main.findEnd(lines, posOne, diff)
        return line
        
        
    def findStart(lines, posTwo, diff):
        line = []
        pos = main.subPositions(posTwo, diff)
        while main.isOnBoard(lines, pos):
            line.append(pos)
            pos = main.subPositions(pos, diff)
        return line
    
    def findEnd(lines, posOne, diff):
        line = []
        pos = main.addPositions(posOne, diff)
        while main.isOnBoard(lines, pos):
            line.append(pos)
            pos = main.addPositions(pos, diff)
        return line
    
    def printBoard(lines, positions):
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if (x,y) in positions:
                    lines[y][x] = '#'
            print(''.join(lines[y]))
    
    def addPositions(posOne, posTwo):
        return (posOne[0]+posTwo[0],posOne[1]+posTwo[1])
    
    def subPositions(posOne, posTwo):
        return (posOne[0]-posTwo[0],posOne[1]-posTwo[1])
    
    def isOnBoard(lines, position):
        if position[0] >= len(lines[0]) or position[0] < 0 or position[1] >= len(lines) or position[1] < 0:
            return False
        return True
    
    
    def clean_lines(lines):
        new_lines = []
        for line in lines:
            new_lines.append(line.strip())
        return new_lines
    
    def split_maps(lines):
        maps ={}
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] != '.':
                    if lines[y][x] not in maps.keys():
                        maps[lines[y][x]] = []
                    maps[lines[y][x]].append((x,y))
        return maps