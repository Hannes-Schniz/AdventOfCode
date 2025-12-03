import re
from tokenize import String


class main:
    # The batteries are arranged into banks; each line of digits in your input corresponds to a single bank of batteries. Within each bank, you need to turn on exactly two batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on. For example, if you have a bank like 12345 and you turn on batteries 2 and 4, the bank would produce 24 jolts. (You cannot rearrange batteries.)
    # You'll need to find the largest possible joltage each bank can produce. In the above example:
    #    In 987654321111111, you can make the largest joltage possible, 98, by turning on the first two batteries.
    #    In 811111111111119, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing 89 jolts.
    #    In 234234234234278, you can make 78 by turning on the last two batteries (marked 7 and 8).
    #    In 818181911112111, the largest joltage you can produce is 92.
    # The total output joltage is the sum of the maximum joltage from each bank, so in this example, the total output joltage is 98 + 89 + 78 + 92 = 357.
    # There are many batteries in front of you. Find the maximum joltage possible from each bank; what is the total output joltage?
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

    # Now, the joltages are much larger:
    #    In 987654321111111, the largest joltage can be found by turning on everything except some 1s at the end to produce 987654321111.
    #    In the digit sequence 811111111111119, the largest joltage can be found by turning on everything except some 1s, producing 811111111119.
    #    In 234234234234278, the largest joltage can be found by turning on everything except a 2 battery, a 3 battery, and another 2 battery near the start to produce 434234234278.
    #    In 818181911112111, the joltage 888911112111 is produced by turning on everything except some 1s near the front.
    # The total output joltage is now much larger: 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619.
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
