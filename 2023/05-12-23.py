import os



#-------------------------------------------------------------------------
#                               Part 1
#-------------------------------------------------------------------------


        


#-------------------------------------------------------------------------
#                               Part 2
#-------------------------------------------------------------------------


        
        
        

#-------------------------------------------------------------------------
#                                General
#-------------------------------------------------------------------------

dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname, 'input_04-12-23.txt')

    

def parseInput(line):
    parsed = []
    values = line.split(":")
    values = values[1].split("|")
    for value in values:
        value = value.strip()
        numbers = []
        for number in value.split(" "):
            if number != "":
                numbers.append(number)
        parsed.append(numbers)
    return parsed
    




with open(file_path, "r") as file:
    
    
    print("Part 1: " + str(runOneResult))
    print("Part 2: " + str(calcResultTwo()))

    