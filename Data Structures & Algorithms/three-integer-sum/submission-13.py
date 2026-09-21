class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, j in enumerate(nums[:-2]):
            if i > 0 and j != nums[i-1]:
                res.extend(self.twosum(j, nums[i+1:]))
        return res
    
    def twosum(self, target, nums):
        l = 0
        r = len(nums) - 1
        res = []

        while l < r:
            if nums[l] + nums[r] == - target:
                res.append([nums[l], nums[r], target])
            elif nums[l] + nums[r] > - target:
                while r > l and nums[r-1] != nums[r]:
                    r -=1
            elif nums[l] + nums[r] < - target:
                while l < r and nums[l+1] != nums[l]:
                    l +=1
        return res
            