from itertools import permutations
class main:
    def solutionOne(lines):
        parsed = main.parse(lines)
        #print(parsed)
        solution = 0
        for nums in parsed:
            calcs = main.calc_numbers(nums[1], False)
            if nums[0] in calcs:
                solution += nums[0]
                
        return solution
    def solutionTwo(lines):
        parsed = main.parse(lines)
        #print(parsed)
        solution = 0
        for nums in parsed:
            calcs = main.calc_numbers(nums[1], True)
            if nums[0] in calcs:
                solution += nums[0]
                
        return solution
    
    def parse(lines):
        parsed = []
        for line in lines:
            temp = line.split(': ')
            nums = []
            for num in temp[1].split(' '):
                nums.append(int(num))
            parsed.append([int(temp[0]), nums])
        return parsed
    
    
    # returns a set of sets of 0's = + and 1's = * 
    def calc_numbers(nums, second):
        new_nums= nums[2:]
        curr = [nums[0]+nums[1], nums[0]*nums[1]]
        if second:
            curr.append(int(str(nums[0])+str(nums[1])))
        for num in new_nums:
            temp = []
            for curr_num in curr:
                temp.append(num+curr_num)
                temp.append(num*curr_num)
                if second:
                    temp.append(int(str(curr_num)+str(num)))
            curr = temp
        return curr
            

            
        
            