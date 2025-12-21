import re


class main:
    REGEX = "(mul\()([0-9]{1,3},[0-9]{1,3})(\))"

    def solutionOne(self, lines: str):
        line = "".join(lines)
        return self.findmult(line)

    def solutionTwo(self, lines):
        solution = 0
        line = "".join(lines)
        first = True
        for section in line.split("don't()"):
            if first:
                solution += self.findmult(section)
                first = False
                continue
            solution += self.findmult("".join(section.split("do()")[1:]))
        return solution

    def findmult(self, line):
        solution = 0
        numbers = re.findall(main.REGEX, line)
        left = [int(x[1].split(",")[0]) for x in numbers]
        right = [int(x[1].split(",")[1]) for x in numbers]
        for i in range(len(left)):
            solution += left[i] * right[i]
        return solution

