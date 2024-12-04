class main:
    def solutionOne(lines):
        return ""
    def solutionTwo(lines):
        cleanLines =[]
        for line in lines:
            cleanLines.append(line.strip())
        old_lines = cleanLines
        cleanLines = main.search_delete(cleanLines)
        main.print_Matrix(old_lines)
        print("--------------------")
        main.print_Matrix(cleanLines)
        while old_lines != cleanLines:
            cleanLines = main.search_delete(cleanLines)
            old_lines = cleanLines
        
        #main.print_Matrix(cleanLines)
        return ''
    
    def search_delete(lines):
        for i in range(len(lines)-1):
            for j in range(len(lines[i])-1):
                lines = main.delete_surrounding(lines,j,i)
        return lines
    
    def delete_surrounding(lines, x, y):
        #xmas
        match lines[y][x]:
            case 'X':
                return main.delete_x(lines, x, y)
            case 'M':
                return main.delete_m(lines, x, y)
            case 'A':
                return main.delete_a(lines, x, y)
            case 'S':
                return main.delete_s(lines, x, y)
        return lines
    
    def delete_x(lines, x, y):
        surrounding = main.getSurrounding(lines, x, y)
        for pos in surrounding:
            if lines[pos[1]][pos[0]] == 'M':
                return lines
        lines[y] = lines[y][:x]+'.'+lines[y][x+1:]
        return lines
    
    def delete_m(lines, x, y):
        surrounding = main.getSurrounding(lines, x, y)
        for pos in surrounding:
            print(y,x,lines[y][x], pos[0], pos[1], lines[pos[1]][pos[0]])
            if lines[pos[1]][pos[0]] == 'X' or lines[pos[1]][pos[0]] == 'A':
                return lines
        lines[y] = lines[y][:x]+'.'+lines[y][x+1:]
        return lines
    
    def delete_a(lines, x, y):
        surrounding = main.getSurrounding(lines, x, y)
        for pos in surrounding:
            if lines[pos[1]][pos[0]] == 'A' or lines[pos[1]][pos[0]] == 'S':
                return lines
        lines[y] = lines[y][:x]+'.'+lines[y][x+1:]
        return lines
    
    def delete_s(lines, x, y):
        surrounding = main.getSurrounding(lines, x, y)
        for pos in surrounding:
            if lines[pos[1]][pos[0]] == 'A':
                return lines
        lines[y] = lines[y][:x]+'.'+lines[y][x+1:]
        return lines          
        
    def getSurrounding(lines, x, y):
        #print(x,y, len(lines), (len(lines[0]) -1), lines[0])
        possibles = [(x+1,y), (x,y+1), (x-1,y), (x, y-1), (x+1,y+1), (x+1,y-1), (x-1, x-1), (x-1,x+1)]
        print(possibles)
        surrounding = []
        for pos in possibles:
            if pos[0] < 0:
                continue
            elif pos[1] < 0:
                continue
            elif pos[1] >= len(lines):
                continue
            elif pos[0] >= (len(lines[0]) -1):
                continue
            surrounding.append(pos)
        print(surrounding)
        #print(lines)
        return surrounding
    
    def print_Matrix(lines):
        for line in lines:
            print(line)
                
            