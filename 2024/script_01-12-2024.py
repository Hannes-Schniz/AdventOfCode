class main:
    def solutionOne(lines):
        left = sorted([int(x.split("   ")[0]) for x in lines])
        right = sorted([int(x.split("   ")[1]) for x in lines])
        solution = 0
        for i in range(len(left)):
            solution+=abs(left[i] - right[i])
        return solution
    def solutionTwo(lines):
        left = sorted([int(x.split("   ")[0]) for x in lines])
        right = sorted([int(x.split("   ")[1]) for x in lines])
        return sum([right.count(x)*x for x in left])     
        
        