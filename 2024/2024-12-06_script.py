class main:
    def solutionOne(lines):
        new_lines= lines
        guard = main.find_guard(lines)
        new_lines[guard[1]] = new_lines[guard[1]][:guard[0]] + 'S' + new_lines[guard[1]][guard[0]+1:]
        steps = main.parole(lines, guard[1], guard[0], 'up', 0)
        while steps[3] != 'done':
            new_lines[steps[1]] = new_lines[steps[1]][:steps[2]] + 'X' + new_lines[steps[1]][steps[2]+1:]
            steps = main.parole(steps[0], steps[1], steps[2], steps[3], steps[4])
        return main.get_count(new_lines)
    def solutionTwo(lines):
        return ""
    
    def print_newLines(lines):
        for line in lines:
            print(line)
    
    def get_count(lines):
        solution = 0
        for line in lines:
            solution += line.count('X') + line.count('S')
        return solution 
    
    def find_guard(lines):
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] == '^':
                    return (x,y)
        return (-1,-1)
    
    def parole(lines, y, x, direction, steps):
        if x-1 < 0 or x+1 >= len(lines[0]) or y-1 < 0 or y+1 >= len(lines):
            return [lines,y,x,'done',steps]
        match direction:
            case 'up':
                if lines[y-1][x] == '#':
                    direction = 'right'
                    return [lines,y,x,direction,steps]
                return [lines,y - 1,x,direction,steps+1]
            case 'right':
                if lines[y][x+1] == '#':
                    direction = 'down'
                    return [lines,y,x,direction,steps]
                return [lines,y,x + 1,direction,steps+1]
            case 'down':
                if lines[y+1][x] == '#':
                    direction = 'left'
                    return [lines,y,x,direction,steps]
                return [lines,y + 1,x,direction,steps+1]
            case 'left':
                if lines[y][x-1] == '#':
                    direction = 'up'
                    return [lines,y,x,direction,steps]
                return [lines,y,x - 1,direction,steps+1]
                
        