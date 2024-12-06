class main:
    def solutionOne(lines):
        return main.get_count(main.traverse(lines), ['X'])
    
    def solutionTwo(lines):
        # 4722 False (too high)
        # 1528 False (too low)
        # 1528 False (too low)
        # 1529 False
        # 1560 False
        # 1540 False
        # 1539 False
        # 1538 False
        # 1664 False
        guard = main.find_guard(lines)
        
        solution = [guard]
        first = main.is_loop(lines, guard[1], guard[0], guard[1], guard[0], 'up')
        if first != False:
            solution.append(first)
        steps = main.parole(lines, guard[1], guard[0], 'up')
        step = 1
        while steps[3] != 'done':
            isLoop = main.is_loop(steps[0], steps[1], steps[2], steps[1], steps[2], steps[3])
            print('checkloop for step', step)
            step +=1
            if isLoop != False and isLoop not in solution:
                solution.append(isLoop)
            steps = main.parole(steps[0], steps[1], steps[2], steps[3])
        #print(solution)
        return len(solution) -1
    
    def traverse(lines):
        guard = main.find_guard(lines)
        steps = main.parole(lines, guard[1], guard[0], 'up')
        while steps[3] != 'done':
            steps = main.parole(steps[0], steps[1], steps[2], steps[3])
        return steps[0]
    
    def print_newLines(lines):
        for line in lines:
            print(line)
    
    def get_count(lines, chars):
        solution = 0
        for line in lines:
            for char in chars:
                solution += line.count(char)
        return solution 
    
    def find_guard(lines):
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] == '^':
                    return (x,y)
        return (-1,-1)
            
    def parole(lines, y, x, direction):
        if x-1 < 0 or x+1 >= len(lines[0]) or y-1 < 0 or y+1 >= len(lines):
            lines[y] = lines[y][:x] + 'X' + lines[y][x+1:]
            return [lines,y,x,'done']
        match direction:
            case 'up':
                if lines[y-1][x] == '#':
                    direction = 'right'
                    return [lines,y,x,direction]
                lines[y] = lines[y][:x] + 'X' + lines[y][x+1:]
                return [lines,y - 1,x,direction]
            case 'right':
                if lines[y][x+1] == '#':
                    direction = 'down'
                    return [lines,y,x,direction]
                lines[y] = lines[y][:x] + 'X' + lines[y][x+1:]
                return [lines,y,x + 1,direction]
            case 'down':
                if lines[y+1][x] == '#':
                    direction = 'left'
                    return [lines,y,x,direction]
                lines[y] = lines[y][:x] + 'X' + lines[y][x+1:]
                return [lines,y + 1,x,direction]
            case 'left':
                if lines[y][x-1] == '#':
                    direction = 'up'
                    return [lines,y,x,direction]
                lines[y] = lines[y][:x] + 'X' + lines[y][x+1:]
                return [lines,y,x - 1,direction]
                
    def is_loop(lines, y, x, start_y, start_x, direction):
        traversed = [(start_x, start_y, direction)]
        new_lines = [[y for y in x] for x in lines]
        obj = ()
        match direction:
            case 'up':
                direction = 'right'
                if y - 1 < 0 or lines[y-1][x] == '#':
                    return False
                new_lines[y-1][x] = '#'
                obj = (x, y-1)
            case 'right':
                direction = 'down'
                if x + 1 >= len(lines[y]) or lines[y][x+1] == '#':
                    return False
                new_lines[y][x+1] = '#'
                obj = (x+1, y)
            case 'down':
                direction = 'left'
                if y +1 >= len(lines) or lines[y+1][x] == '#':
                    return False
                new_lines[y+1][x] = '#'
                obj = (x,y+1)
            case 'left':
                direction = 'up'
                if x - 1 < 0 or lines[y][x-1] == '#':
                    return False
                new_lines[y][x-1] = '#'
                obj = (x-1,y)
        #print('loop for', start_x, start_y, direction)
        while direction != 'done':
            traversed.append((x,y, direction))
            if x-1 < 0 or x+1 >= len(new_lines[0]) or y-1 < 0 or y+1 >= len(new_lines):
                return False
            match direction:
                case 'up':
                    if new_lines[y-1][x] == '#':
                        direction = 'right'
                        continue
                    if (x,y-1, direction) in traversed:
                        #print(traversed)
                        return obj
                    y = y - 1
                case 'right':
                    if new_lines[y][x+1] == '#':
                        direction = 'down'
                        continue
                    if (x+1,y, direction) in traversed:
                        #print(traversed)
                        return obj
                    x = x + 1
                case 'down':
                    if new_lines[y+1][x] == '#':
                        direction = 'left'
                        continue
                    if (x,y+1, direction) in traversed:
                        #print(traversed)
                        return obj
                    y = y + 1
                case 'left':
                    if new_lines[y][x-1] == '#':
                        direction = 'up'
                        continue
                    if (x-1,y, direction) in traversed:
                        #print(traversed)
                        return obj
                    x = x - 1
            
        return False
    
    
        