import re
from tokenize import String


class main:
    def solutionOne(lines):
        erg = 0
        for line in lines:
            line = line.strip()
            numbers = {
                "1": [],
                "2": [],
                "3": [],
                "4": [],
                "5": [],
                "6": [],
                "7": [],
                "8": [],
                "9": [],
            }
            for i in range(len(line)):
                numbers[line[i]] = numbers[line[i]] + [i]

            for key in sorted(numbers.keys(), reverse=True):
                if numbers[key] == []:
                    continue
                if len(numbers[key]) == 1 and numbers[key][0] == len(line) - 1:
                    continue
                prefix = min(numbers[key])

                break
            suffix = -1

            for key in sorted(numbers.keys(), reverse=True):
                for pos in numbers[key]:
                    if pos > prefix:
                        suffix = pos
                        break
                if suffix != -1:
                    break

            highest = int(f"{line[prefix]}{line[suffix]}")
            erg += highest

        return erg

    def solutionTwo(lines):
        erg = 0
        for line in lines:
            line = line.strip()

            delSteps = len(line) - 11
            num = [0] * 12
            step = 0
            for i in range(len(line)):
                step += 1
                smaller = False
                for j in [x for x in range(len(num)) if x >= step - delSteps]:
                    if smaller == True:
                        num[j] = 0
                        continue

                    if int(line[i]) > num[j]:
                        num[j] = int(line[i])
                        smaller = True
            number = int("".join(str(x) for x in num))
            erg += number
        return erg
