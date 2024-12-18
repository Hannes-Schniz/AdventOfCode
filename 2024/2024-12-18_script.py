class main:
    def solutionOne(lines):
        boardSize = 70
        parsed = main.parse(lines,1024)
        board = main.buildBoard(parsed, boardSize+1)
        main.printBoard(board)
        path = main.bfs(board,(0,0),(boardSize,boardSize))
        pathmap = main.buildPath(board,path)
        main.printBoard(pathmap)
        return len(path)-1
    def solutionTwo(lines):
        boardSize = 70
        line = 1024
        parsed = main.parse(lines,line)
        board = main.buildBoard(parsed, boardSize+1)
        path = main.bfs(board,(0,0),(boardSize,boardSize))
        while path != []:
            next = main.parseOne(lines[line])
            print(next)
            board = main.alterBoard(board,next)
            path = main.bfs(board,(0,0),(boardSize,boardSize))
            line += 1
        print(lines[line-1])
        return 
    
    
    def parseOne(line):
        splitted = line.split(',')
        return(int(splitted[0]),int(splitted[1]))
    
    def alterBoard(board,object):
        board[object[1]][object[0]] = '#'
        return board
    
    def parse(lines,limit):
        fallen = []
        for line in lines:
            cords = line.split(',')
            fallen.append((int(cords[0]), int(cords[1])))
            if len(fallen) == limit:
                break
        return sorted(set(fallen))
    
    def buildBoard(fallen,size):
        board = []
        for y in range(size):
            row = []
            for x in range(size):
                if (x,y) in fallen:
                    row.append('#')
                    continue
                row.append('.')
            board.append(row)
        return board
    
    def buildPath(board, path):
        for y in range(len(board)):
            for x in range(len(board[y])):
                if (x,y) not in path:
                    continue
                board[y][x] = 'O'
        return board
    
    def printBoard(board):
        for row in board:
            print(''.join(row))
            
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
            
    def bfs(board, start, end):
        visited = set()
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node in visited:
                continue
            neighbors = main.findNeighbors(board,node)
            for neighbor in neighbors:
                if board[neighbor[1]][neighbor[0]] != '#':
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                
                if neighbor == end:
                    return new_path
            visited.add(node)
        return []
                
            
            
                
            
                