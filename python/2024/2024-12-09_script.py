class main:
    def solutionOne(lines):
        return main.calcHash(main.compress(main.buildMap(main.parse(lines[0].strip()))))
    def solutionTwo(lines):
        parsed = main.parse(lines[0].strip())
        map = main.buildMap(parsed)
        blockMap = main.parseBlocks(map)
        solution = main.compressBlocks(blockMap)
        return main.calcHashTwo(solution)
    
    def calcHashTwo(map):
        solution = 0
        count = 0
        for element in map:
            if len(element) == 0:
                continue
            for pos in element:
                if pos == '.':
                    count += 1
                    continue
                solution += count*pos
                count += 1
        return solution
    
    def calcHash(map):
        solution = 0
        for i in range(len(map)):
            if map[i] == '.':
                break
            solution += i*map[i]
        return solution 
    
    
    def parse(line):
        blocks = []
        for char in line:
            blocks.append(int(char))
        return blocks
    
    def parseBlocks(line):
        blocks = []
        curr = []
        for char in line:
            if char not in curr and len(curr) != 0:
               blocks.append(curr)
               curr = [char]
               continue
            curr.append(char)
        blocks.append(curr)
        return blocks
    
    
    def buildMap(blocks):
        count = 0
        map = []
        filler = 0
        blockNumber = 0
        for block in blocks:
            if count % 2 == 0:
                filler = blockNumber
                blockNumber += 1
            else:
                filler = '.'
            for i in range(block):
                   map.append(filler)
            count += 1
        return map
    
    def hasGaps(map):
        found = False
        for e in map:
            if e == '.':
                found = True
            if found and e != '.':
                return True
        return False
    
    def compress(map):
        open = []
        blocked = []
        for i in range(len(map)):
            if map[i] == '.':
                open.append(i)
            else:
                blocked.append(i)
        blocked = sorted(blocked,reverse=True)
        idx = 0
        for spot in open:
            if idx >= len(blocked) or not main.hasGaps(map):
                break
            map[spot] = map[blocked[idx]]
            map[blocked[idx]] = '.'
            idx += 1
            
        return map
    
    def findSpaces(map):
        end = 0
        start = -1
        positions = []
        for pos in range(len(map)):
            if map[pos] == '.' and start == -1:
                start = pos
            if start != -1 and map[pos] != '.':
                end = pos -1
                positions.append((start, end))
                start = -1
        return positions
    
    def replace(map,toReplace , replacee ):
        #print(map[toReplace], map[replacee])
        delta = 0
        newElement = []
        front = False
        back = False
        for e in map[replacee]:
            newElement.append('.')
        map[toReplace] = map[toReplace][len(map[replacee]):]
        if len(map[toReplace]) == 0:
            delta += 1     
        map.insert(toReplace, map[replacee])
        map[replacee+1] = newElement
        #print(map)
        delta -= 1
        if len(map[replacee]) > 0 and map[replacee][0] == '.':
            map[replacee+1] += map[replacee]
            front = True
        if replacee +2 < len(map) and map[replacee+2][0] == '.' :
            map[replacee+1] += map[replacee+2]
            back = True
        if front:
            del map[replacee]
            delta += 1
        if back:
            del map[replacee+1]
            delta += 1
        return ([x for x in map if x != []], delta)
    
    def compressBlocks(blockMap):
        #newMap = blockMap
        
        i = len(blockMap) -1
        while i > 0:
            j = 0
            print(blockMap)
            if blockMap[i][0] == '.':
                i-= 1
                continue
            while i > j:
                if blockMap [j][0] != '.':
                    j += 1
                    continue
                #print(blockMap[i], blockMap[j])
                if len(blockMap[i]) <= len(blockMap[j]) and blockMap[j][0] == '.' and blockMap[i][0] != '.':
                    temp = main.replace(blockMap, j, i) 
                    blockMap = temp[0]
                    i -= temp[1]
                    break
                j += 1
            i -= 1
        return blockMap
    
                
                        
                
        