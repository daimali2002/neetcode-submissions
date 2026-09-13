class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = 0;
        nums.sort()
        for i in nums:
            if i != num:
                return num
            num += 1
        return num
        
        