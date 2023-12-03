import os
dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname, 'input_02-12-23.txt')


def analyseSurround(lines, idx):
    # [., ., .] -1/-1 0/-1 1/-1
    # [., x, .] -1/0 0/0 1/0
    # [., ., .] -1/1 0/1 1/1
    
    startIDX = idx - 1
    endIDX = idx + 1
    
    if startIDX < 0:
        startIDX = 0
    if endIDX > len(lines):
        endIDX = len(lines)
    
    for i in range(startIDX, endIDX):
        print(lines[i])
    
idx = 0

with open(file_path, "r") as file:
    while idx < 10:
        # gets previous, curr and next line
        lines = ["", "", ""]
        if idx != 0:
            lines[1]= lines[2]
        lines[2] = file.readline()
        
        # gets the special char
        for c in lines[1]:
            if c.isnumeric() == False and c != ".":
                analyseSurround(lines, idx)
        
        lines[0] = lines[1]
        idx += 1