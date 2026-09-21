class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        length = 1
        maxx = 0
        
        
        for i in range(len(nums)):
            while (nums[i] + length) in s and (nums[i] - 1) not in s: 
                length += 1
            maxx = max(maxx, length)
            length = 1
        
        return maxx
        
        