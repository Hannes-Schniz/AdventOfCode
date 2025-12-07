import threading
from ast import arg


class main:
    def solutionOne(lines):
        erg = -1
        cols = []
        for pos in range(len(lines[0])):
            if lines[0][pos] == "S":
                cols = [pos]
                break

        for pos in range(len(lines)):
            toRemove = []
            toAdd = []
            for col in cols:
                if col < 0 or col >= len(lines[pos]):
                    toRemove.append(col)
                    continue
                if lines[pos][col] == "^":
                    toRemove.append(col)
                    if col - 1 > 0 and col - 1:
                        toAdd.append(col - 1)
                    if col + 1 < len(lines[pos]):
                        toAdd.append(col + 1)
                    erg += 1
            cols = [x for x in cols if x not in toRemove]
            toAdd = set([x for x in toAdd if x not in cols])
            cols.extend(toAdd)
            cols = sorted(cols)
        return erg + 1

    def validate(curr, vecs):
        for i in reversed(range(0, curr[1])):
            if (curr[0] - 1, i) in vecs:
                return True
            if (curr[0] + 1, i) in vecs:
                return True
            if (curr[0], i) in vecs:
                break
        print((curr[0], i))
        return False

    def solutionTwo(lines):
        erg = -1
        vecs = []
        start = 0
        for pos in range(len(lines[0])):
            if lines[0][pos] == "S":
                start = pos
                break
        for line in range(len(lines)):
            for pos in range(len(lines[line])):
                if lines[line][pos] == "^":
                    vecs.append((pos, line))
        oldVecs = vecs.copy()
        vecs = [x for x in vecs if main.validate(x, vecs) or x == (start, 0)]
        print([x for x in vecs if x not in oldVecs])
        lastPos = [(start, 0)]
        streams = 0
        while True:
            currVec = lastPos.pop(0)
            if currVec[1] == len(lines):
                break
            if currVec in vecs:
                if currVec[0] - 1 >= 0:
                    lastPos.append((currVec[0] - 1, currVec[1] + 1))
                    streams += 1

                if currVec[0] + 1 <= len(lines[0]):
                    streams += 1
                    lastPos.append((currVec[0] + 1, currVec[1] + 1))
            else:
                lastPos.append((currVec[0], currVec[1] + 1))
            print(currVec[1], end="\r")
        print(streams)

        print(len(lastPos) + 1)

        return erg
