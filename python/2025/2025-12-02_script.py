import re


class main:
    def solutionOne(lines):
        ranges = [x for x in lines[0].split(",")]
        erg = 0
        for rng in ranges:
            start = int(rng.split("-")[0])
            end = int(rng.split("-")[1])
            for i in [x for x in range(start, end + 1) if len(str(x)) % 2 == 0]:
                i = str(i)
                prefix = i[0 : len(i) // 2]
                suffix = i[(len(i) // 2) :]
                # print(i, prefix, suffix)
                if prefix == suffix:
                    erg += int(i)

        return erg

    def solutionTwo(lines):
        ranges = [x for x in lines[0].split(",")]
        erg = 0
        found = []
        for rng in ranges:
            start = int(rng.split("-")[0])
            end = int(rng.split("-")[1])
            for i in range(start, end + 1):
                i = str(i)
                for n in range(1, len(i) // 2 + 1):
                    if len(i) % n != 0:
                        continue
                    new_string = i[:n] * (len(i) // n)
                    if (
                        int(new_string) > int(end)
                        or new_string in found
                        or int(new_string) < int(start)
                    ):
                        continue
                    erg += int(new_string)
                    found.append(new_string)
        return erg
