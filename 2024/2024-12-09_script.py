class main:
    def solutionOne(lines):
        lines = lines[0].strip()
        blocks = main.parse(lines)
        map = main.buildMap(blocks)
        compressed = main.compress(map)
        return main.calcHash(compressed)
    def solutionTwo(lines):
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
        