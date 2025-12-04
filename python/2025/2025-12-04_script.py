class main:
    def solutionOne(lines):
        erg = 0
        map = []
        for line in lines:
            line = line.strip()
            map.append([x for x in line])

        for i in range(len(map)):
            for j in range(len(map[i])):
                count = 0
                if map[i][j] == ".":
                    continue
                if i - 1 >= 0 and map[i - 1][j] == "@":
                    count += 1
                if i < len(map) - 1 and map[i + 1][j] == "@":
                    count += 1

                if j < len(map[j]) - 1 and map[i][j + 1] == "@":
                    count += 1
                if j - 1 >= 0 and map[i][j - 1] == "@":
                    count += 1
                if j - 1 >= 0 and i - 1 >= 0 and map[i - 1][j - 1] == "@":
                    count += 1
                if j < len(map[j]) - 1 and i - 1 >= 0 and map[i - 1][j + 1] == "@":
                    count += 1
                if j - 1 >= 0 and i < len(map) - 1 and map[i + 1][j - 1] == "@":
                    count += 1
                if (
                    j < len(map[j]) - 1
                    and i < len(map) - 1
                    and map[i + 1][j + 1] == "@"
                ):
                    count += 1

                if count < 4:
                    erg += 1

        return erg

    def recTwo(erg, map):
        newErg = erg
        newMap = map
        for i in range(len(map)):
            for j in range(len(map[i])):
                count = 0
                if map[i][j] == ".":
                    continue
                if i - 1 >= 0 and map[i - 1][j] == "@":
                    count += 1
                if i < len(map) - 1 and map[i + 1][j] == "@":
                    count += 1

                if j < len(map[j]) - 1 and map[i][j + 1] == "@":
                    count += 1
                if j - 1 >= 0 and map[i][j - 1] == "@":
                    count += 1
                if j - 1 >= 0 and i - 1 >= 0 and map[i - 1][j - 1] == "@":
                    count += 1
                if j < len(map[j]) - 1 and i - 1 >= 0 and map[i - 1][j + 1] == "@":
                    count += 1
                if j - 1 >= 0 and i < len(map) - 1 and map[i + 1][j - 1] == "@":
                    count += 1
                if (
                    j < len(map[j]) - 1
                    and i < len(map) - 1
                    and map[i + 1][j + 1] == "@"
                ):
                    count += 1

                if count < 4:
                    erg += 1
                    newMap[i][j] = "."
        # print("".join([f"{''.join(x)}\n" for x in newMap]))
        if newErg == erg:
            return erg
        else:
            return main.recTwo(erg, newMap)

    def solutionTwo(lines):
        map = []
        for line in lines:
            line = line.strip()
            map.append([x for x in line])

        return main.recTwo(0, map)
