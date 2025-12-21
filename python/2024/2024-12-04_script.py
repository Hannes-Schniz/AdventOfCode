import re


class main:
    def solutionTwo(self, lines):
        cleanLines = []
        solution = 0
        for line in lines:
            cleanLines.append(line.strip())
        for i in range(1, len(cleanLines) - 1):
            for j in range(1, len(cleanLines[i]) - 1):
                if lines[i][j] != "A":
                    continue
                solution += self.getX(lines, i, j)
        return solution

    def solutionOne(self, lines):
        cleanLines = []
        for line in lines:
            cleanLines.append(line.strip())
        max_col = len(cleanLines[0])
        max_row = len(cleanLines)
        cols = [[] for _ in range(max_col)]
        rows = [[] for _ in range(max_row)]
        fdiag = [[] for _ in range(max_row + max_col - 1)]
        bdiag = [[] for _ in range(len(fdiag))]
        min_bdiag = -max_row + 1

        for x in range(max_col):
            for y in range(max_row):
                cols[x].append(lines[y][x])
                rows[y].append(lines[y][x])
                fdiag[x + y].append(lines[y][x])
                bdiag[x - y - min_bdiag].append(lines[y][x])
        return (
            self.find_XMAS(cols)
            + self.find_XMAS(rows)
            + self.find_XMAS(fdiag)
            + self.find_XMAS(bdiag)
        )

    def find_XMAS(self, lines):
        solution = 0
        for line in lines:
            curr = "".join(line)
            solution += len(re.findall("XMAS", curr))
            solution += len(re.findall("SAMX", curr))
        return solution

    def getX(self, lines, i, j):
        solution = 0
        lt = "".join(sorted([lines[i + 1][j + 1], lines[i - 1][j - 1]]))
        rt = "".join(sorted([lines[i + 1][j - 1], lines[i - 1][j + 1]]))
        solution += len(re.findall("MS", lt))
        solution += len(re.findall("MS", rt))
        if solution == 2:
            return 1
        return 0

