class main:
    def solutionOne(lines):
        solution = 0
        map = main.parseLines(lines)
        #print(map)
        starts = main.findStarts(map)
        for start in starts:
            headValue = len(main.discover(map,start,[], [])) -1 
            #print(start, headValue)
            solution += headValue
        return solution
    def solutionTwo(lines):
        solution = 0
        map = main.parseLines(lines)
        #print(map)
        starts = main.findStarts(map)
        for start in starts:
            headValue = main.discoverPaths(map,start) 
            print(start, headValue)
            solution += headValue
        return solution
    
    def parseLines(lines):
        map = []
        for line in lines:
            line = line.strip()
            curr = []
            for char in line:
                curr.append(int(char))
            map.append(curr)
            
        return map
    
    def findStarts(map):
        starts = []
        for y in range(len(map)):
            for x in range(len(map[y])):
                if not map[y][x] == 0:
                    continue
                starts.append((x,y))
        return starts
    
    def findNeighbors(map, position):
        #(-1,-1)(0,-1)(1,-1)
        #(-1,0) (0,0) (1,0)
        #(-1,1) (0,1) (1,1)
        neighbors = []
        masks = [(0,-1),(-1,0), (1,0), (0,1)]
        for mask in masks:
            masked = (position[0]+mask[0], position[1]+mask[1])
            if masked[0] < 0 or masked[1] < 0 or masked[0] >= len(map[position[0]]) or masked[1] >= len(map):
                continue
            neighbors.append(masked)
        return neighbors
    
    def discover(map, position, discovered, ends):
        if map[position[1]][position[0]] == 9 and position not in ends:
            return position
        for neighbor in [x for x in main.findNeighbors(map, position) if x not in discovered]:
            discovered.append(position)
            if map[neighbor[1]][neighbor[0]] == map[position[1]][position[0]] +1:
                end = main.discover(map,neighbor, discovered, ends)
                if end != [] and end not in ends:
                    ends.append(end)
        return ends
    
    def discoverPaths(map, position):
        sol = 0
        if map[position[1]][position[0]] == 9:
            return 1
        for neighbor in main.findNeighbors(map, position):
            if map[neighbor[1]][neighbor[0]] == map[position[1]][position[0]] +1:
                sol += main.discoverPaths(map,neighbor)
        return sol