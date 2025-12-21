class main:
    def solutionOne(self, lines):
        erg = 0
        map = [[int(x)] for x in lines[0].strip().split()]

        for i in range(1, len(lines) - 1):
            elements = [int(x) for x in lines[i].strip().split()]
            for j in range(len(elements)):
                map[j].append(elements[j])
        operators = [x for x in lines[len(lines) - 1].strip().split()]
        for i in range(len(operators)):
            if operators[i] == "+":
                temp = 0
                for j in range(len(map[i])):
                    temp += map[i][j]
                erg += temp
            elif operators[i] == "*":
                temp = 1
                for j in range(len(map[i])):
                    temp *= map[i][j]
                erg += temp
        return erg

    def solutionTwo(self, lines):
        erg = 0
        numbers = []
        pos = 0
        operator = ""
        for idx in reversed(range(len(lines[0]))):
            number = ""
            for line in lines:
                if idx >= len(line) or line[idx] == " ":
                    if pos == len(lines):
                        number = ""
                    continue
                if line[idx] in ["+", "*"]:
                    operator = line[idx]
                if line[idx] in [str(x) for x in range(10)]:
                    number = f"{line[idx]}{number}"
                pos += 1
                if pos >= len(lines):
                    pos = 0
            if number:
                numbers.append(number[::-1])
            if operator:
                if operator == "+":
                    temp = 0
                    for calc in numbers:
                        temp += int(calc)
                    erg += temp
                elif operator == "*":
                    temp = 1
                    for calc in numbers:
                        temp *= int(calc)
                    erg += temp
                numbers = []
                operator = ""

        return erg
