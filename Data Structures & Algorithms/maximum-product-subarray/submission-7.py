class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #case 1, there is a zero in there in which case i want to split the problem into multiple problems

        #case 2, no zeros but has negative numbers, if even amount of negative numbers, then prod of all things

        #case 3, no zeros but has negative numbers, if odd then, prod of all before/after except last negative, 
        #                                                        prod of all before/after except fist negative

        negcount = 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return float('-inf')
        totprod = 1
        firstneg = float('+inf')
        lastneg = float('-inf')
        for c , i in enumerate(nums):
            if i == 0:
                return max(self.maxProduct(nums[:c]),  self.maxProduct(nums[c+1:]), 0)
            elif i < 0:
                negcount += 1
                firstneg = min(firstneg,c)
                lastneg = max(lastneg, c)
            totprod *= i

        if negcount%2 ==0:
            return totprod
        
        firsthalf = nums[0]
        lasthalf = nums[len(nums)-1]
#WHAT IF ONLY ONE NEG
        for i in range(1,lastneg):
            firsthalf *= nums[i]
        for i in range(firstneg + 1,len(nums)-1):
            lasthalf *= nums[i]

        return max(firsthalf, lasthalf)
            
        

        


        
        


        

        
        