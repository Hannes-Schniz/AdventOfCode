class main:
    def solutionOne(lines):
        start = 50
        count = 0
        for line in lines:
            direction = line[0]
            turns = int(line[1:])
            if direction == "L":
                start = (start - turns) % 100
            if direction == "R":
                start = (start + turns) % 100
            if start == 0:
                count += 1
        return count

    def solutionTwo(lines):
        start = 50
        count = 0
        for line in lines:
            direction = line[0]
            turns = int(line[1:])
            if direction == "L":
                while turns > 0:
                    start -= 1
                    turns -= 1
                    if start == 0:
                        count += 1
                    if start < 0:
                        start = 99

            if direction == "R":
                while turns > 0:
                    start += 1
                    turns -= 1
                    if start > 99:
                        start = 0
                    if start == 0:
                        count += 1
        return count
