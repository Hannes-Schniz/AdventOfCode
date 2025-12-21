from operator import itemgetter


class main:
    def solutionOne(self, lines):
        erg = 0
        idx = 0
        line = lines[idx].strip()
        ranges = []
        while line != "":
            ranges.append([int(x) for x in line.split("-")])
            idx += 1
            line = lines[idx].strip()
        ranges = sorted(ranges, key=itemgetter(0))
        # print(ranges)
        idx += 1
        number = int(lines[idx].strip())
        while number:
            validRanges = [x for x in ranges if x[0] <= number and x[1] >= number]
            if len(validRanges) > 0:
                erg += 1
            idx += 1
            if idx >= len(lines):
                break
            number = int(lines[idx].strip())
        return erg

    def recTwo(self, ranges):
        changed = False
        newRanges = []
        skip = False
        for i in range(len(ranges) - 1):
            changed = False
            if skip:
                skip = False
                continue
            skip = False
            start = ranges[i][0]
            end = ranges[i][1]
            for j in range(i + 1, len(ranges)):
                if (ranges[i][0] >= ranges[j][0] and ranges[i][0] <= ranges[j][1]) or (
                    ranges[j][0] >= ranges[i][0] and ranges[j][0] <= ranges[i][1]
                ):
                    end = max(ranges[i][1], ranges[j][1])
                    changed = True
                elif (
                    ranges[i][1] >= ranges[j][0] and ranges[i][1] <= ranges[j][1]
                ) or (ranges[j][1] >= ranges[i][0] and ranges[j][1] <= ranges[i][1]):
                    start = min(ranges[i][0], ranges[j][0])
                    changed = True

                if changed:
                    if (
                        ranges[i][0] >= ranges[j][0] and ranges[i][1] <= ranges[j][1]
                    ) or (
                        ranges[j][0] >= ranges[i][0] and ranges[j][1] <= ranges[i][1]
                    ):
                        skip = True
                    break
            newRanges.append([start, end])

        if not changed:
            newRanges.append(ranges[len(ranges) - 1])
        if newRanges != ranges:
            return self.recTwo(newRanges)
        return newRanges

    def solutionTwo(self, lines):
        erg = 0
        idx = 0
        line = lines[idx].strip()
        ranges = []
        while line != "":
            ranges.append([int(x) for x in line.split("-")])
            idx += 1
            line = lines[idx].strip()
        ranges = sorted(ranges, key=itemgetter(0))
        ranges = self.recTwo(ranges)
        for element in ranges:
            erg += element[1] - element[0] + 1
        return erg
