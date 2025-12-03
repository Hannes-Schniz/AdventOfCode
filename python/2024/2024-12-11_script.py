class main:
    def solutionOne(lines):
        parsed = main.parse(lines[0])
        for i in range(25):
            parsed = main.decide(parsed)
        return len(parsed)
    def solutionTwo(lines):
        return ''
    def parse(line):
        parsed = []
        for number in line.split(' '):
            parsed.append(int(number))
        return parsed
    
    def decide(numbers):
        newNumbers = []
        for number in numbers:
            if number == 0:
                #print(number, 0)
                newNumbers.append(1)
            elif len(str(number)) % 2 == 0:
                half = int(len(str(number))/2)
                #print(half)
                newNumbers.append(int(str(number)[:half]))
                newNumbers.append(int(str(number)[half:]))
            else:
                #print(number, number*2024)
                newNumbers.append(number*2024)
                
        return newNumbers
                