class main:
    def solutionOne(lines):
        return main.calcHash(main.compress(main.buildMap(main.parse(lines[0].strip()))))
    def solutionTwo(lines):
        parsed = main.parse(lines[0].strip())
        map = main.buildMap(parsed)
        solution = main.compressBlocks(map)
        print(''.join([str(x) for x in solution]))
        return ''
    
    
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
    
    def findSpace(map):
        end = 0
        start = -1
        for pos in range(len(map)):
            if map[pos] == '.' and start == -1:
                start = pos
            if start != -1 and map[pos] != '.':
                end = pos -1
                break
        return (start,end)
    
    #toReplace: (start, end) of range that has to be replaced
    #replacee: Array of indexes of the map where the numbers filling the spots are located
    def replace(map,toReplace , replacee ):
        count = 0
        for i in range(toReplace[0], toReplace[1]):
            if count >= len(replacee):
                break
            map[i] = map[replacee[count]]
            map[replacee[count]] = '.'
            count += 1
        return map
    
    def compressBlocks(map):
        blocked = []
        for i in range(len(map)):
            if not map[i] == '.':
                blocked.append((i,map.count(map[i])))
        blocked = sorted(blocked, reverse=True)
        currSpace = main.findSpace(map)
        for pos in sorted(range(len(map)-1), reverse=True):
            if not map[pos] == '.':
                block = [x for x in map if x == map[pos]]
                #print(block)
                print(currSpace)
                if len(block) > (currSpace[1] - currSpace[0] + 1):
                    pos -= len(block)
                    continue
                map = main.replace(map, currSpace, range(pos, pos+len(block)))
                currSpace = main.findSpace(map)
                pos -= len(block)
        return map
                        
                
        