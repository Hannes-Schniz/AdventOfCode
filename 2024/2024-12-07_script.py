class main:
    def solutionOne(lines):
        return ''
    def solutionTwo(lines):
        return '' 
    
    def parse(lines):
        parsed = []
        for line in lines:
            temp = lines.split(': ')
            curr = [int(temp[0])]
            for num in temp[1].split(' '):
                curr.append(int(num))
            parsed.append(curr)
        return parsed
            