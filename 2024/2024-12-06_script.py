class main:
    def solutionOne(lines):
        return main.get_count(main.traverse(lines), ['X'])
    def solutionTwo(lines):
        return ""
    
    def traverse(lines):
        guard = main.find_guard(lines)
        steps = main.parole(lines, guard[1], guard[0], 'up', 0)
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
                
        