class main:
    def parser(self, lines):
        return [[int(y) for y in x.split(" ")] for x in lines]

    def checkLine(self, line, dec):
        errors = []
        for i in range(len(line) - 1):
            if line[i] > line[i + 1] and not dec:
                # print("----------wrong order----------")
                # print(line, "Error at", line[i], line[i+1])
                errors.append(i - 1)
            if line[i] < line[i + 1] and dec:
                # print("----------wrong order----------")
                # print(line, "Error at", line[i], line[i+1])
                errors.append(i - 1)
            if abs(line[i] - line[i + 1]) > 3 or abs(line[i] - line[i + 1]) == 0:
                # print("----------wrong order----------")
                # print(line, "Error at", line[i], line[i+1])
                errors.append(i)
        if len(errors) > 0:
            return errors
        return True

    def getDESC(self, line):
        if line[0] > line[1]:
            return True
        return False

    def solutionOne(self, lines):
        parsed = self.parser(lines)
        solution = 0
        for line in parsed:
            if self.checkLine(line, self.getDESC(line)) is True:
                solution += 1
        return solution

    def solutionTwo(self, lines):
        parsed = self.parser(lines)
        solution = 0
        for line in parsed:
            checked = self.checkLine(line, self.getDESC(line))
            if checked is True:
                solution += 1
            else:
                for i in range(len(line)):
                    # print(line)
                    newLine = list(line)
                    del newLine[i]
                    # print(line)
                    if self.checkLine(newLine, self.getDESC(newLine)) is True:
                        solution += 1
                        break
        return solution

