class main:
    def solutionOne(lines):
        return main.get_count(main.traverse(lines)[0], ['X'])
    
    def solutionTwo(lines):
        guard = main.find_guard(lines)
        route = main.traverse(lines)[1]
        solution = 0
        first = main.is_loop(lines, guard[1], guard[0], guard[1], guard[0], 'up')
        if first != False:
            solution.append(first)
        step = 1
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                print('running position', step)
                step += 1
                if (x,y) not in route:
                    continue
                new_lines = [[y for y in x] for x in lines]
                if new_lines[y][x] == '#':
                    continue
                if (x,y) != guard[1]:
                    new_lines[y][x] = 'O'   
                if main.is_loop(new_lines, guard[1], guard[0], guard[1], guard[0], 'up'):
                    solution += 1
        return solution
    
    def traverse(lines):
        guard = main.find_guard(lines)
        steps = main.parole(lines, guard[1], guard[0], 'up')
        route = [guard]
        while steps[3] != 'done':
            route.append((steps[2],steps[1]))
            steps = main.parole(steps[0], steps[1], steps[2], steps[3])
        return [steps[0],route]
    
    def print_newLines(lines):
        for line in lines:
            print(''.join(line))
    
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
                
    def is_loop(new_lines, y, x, start_y, start_x, direction):
        traversed = []
        #print('loop for', start_x, start_y, direction)
        while direction != 'done':
            traversed.append((x,y, direction))
            if x-1 < 0 or x+1 >= len(new_lines[0]) or y-1 < 0 or y+1 >= len(new_lines):
                return False
            match direction:
                case 'up':
                    if new_lines[y-1][x] == '#' or new_lines[y-1][x] == 'O':
                        direction = 'right'
                        continue
                    if (x,y-1, direction) in traversed:
                        
                        return True
                    y = y - 1
                case 'right':
                    if new_lines[y][x+1] == '#' or new_lines[y][x+1] == 'O':
                        direction = 'down'
                        continue
                    if (x+1,y, direction) in traversed:
                        
                        return True
                    x = x + 1
                case 'down':
                    if new_lines[y+1][x] == '#' or new_lines[y+1][x] == 'O':
                        direction = 'left'
                        continue
                    if (x,y+1, direction) in traversed:
                        
                        return True
                    y = y + 1
                case 'left':
                    if new_lines[y][x-1] == '#' or new_lines[y][x-1] == 'O':
                        direction = 'up'
                        continue
                    if (x-1,y, direction) in traversed:
                        
                        return True
                    x = x - 1
            
        return False
    
    
        