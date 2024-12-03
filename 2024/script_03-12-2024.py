import re
class main:
    REGEX = '(mul\()([0-9]{1,3},[0-9]{1,3})(\))'
    DO_REGEX = '(do\(\).*?)(.*?)(don\'t\(\))'
    FIRST_DO = '(.*?)(don\'t\(\))'
    def solutionOne(lines):
        solution = 0
        for line in lines:
            numbers = re.findall(main.REGEX, line)
            left = [int(x[1].split(",")[0]) for x in numbers]
            right = [int(x[1].split(",")[1]) for x in numbers]
            for i in range(len(left)):
                solution += left[i] * right[i]
        return solution
    def solutionTwo(lines):
        #92410392 False
        solution = 0
        for line in lines:
            section = re.findall(main.FIRST_DO, line)[0]
            solution += main.solutionOne(section)
            section = line.split("don't()")[-1].split("do()")[1:]
            section = ''.join(section)
            print("--------")
            print(section)
            solution += main.solutionOne(section)
            sections = re.findall(main.DO_REGEX, line)
            for section in sections:
                solution += main.solutionOne(section)
        return solution