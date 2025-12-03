import math
class main:
    def solutionOne(lines):
        parsed = main.parse(lines)
        
        rows = parsed[1]
        rules = parsed[0]
        solution =0
        for row in rows:
            safe = True
            for rule in rules:
                if rule[0] not in row or rule[1] not in row:
                    continue
                if row.index(rule[0]) > row.index(rule[1]):
                    safe = False
                
            if safe:
                solution += int(row[math.floor(len(row) / 2)])
        
        return solution
    
    def solutionTwo(lines):
        parsed = main.parse(lines)
        
        rows = parsed[1]
        rules = parsed[0]
        solution = 0
        
        for row in rows:
            safe = True
            for rule in rules:
                if rule[0] not in row or rule[1] not in row:
                    continue
                if row.index(rule[0]) > row.index(rule[1]):
                    safe = False
                
            if not safe:          
                solution += int(row[math.floor(len(main.order(row, rules)) / 2)])
        
        return solution
    
    
    def order(row, rules):
        
        redo = False
        for rule in rules:
            if rule[0] not in row or rule[1] not in row:
                continue
            if row.index(rule[0]) > row.index(rule[1]):
                tmp = row[row.index(rule[0])]
                row[row.index(rule[0])] = row[row.index(rule[1])]
                row[row.index(rule[1])] = tmp
                redo = True
        if redo:
            return main.order(row,rules)
                    
        return row
    
    def parse(lines):
        rules = []
        rows = []
        for line in lines:
            line = line.strip()
            if len(line.split('|')) > 1:
                rules.append(line.split('|'))
            elif len(line.split(',')) > 1:
                rows.append(line.split(','))
        return (rules,rows)