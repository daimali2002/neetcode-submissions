class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, j in enumerate(nums[:-2]):
            if i == 0 or j != nums[i-1]:
                res.extend(self.twosum(j, nums[i+1:]))
        return res
    
    def twosum(self, target, nums):
        l, r , res = 0, len(nums) - 1, []
        equal = nums[l] + nums[r] + target

        while l < r:
            if equal == 0:
                res.append([nums[l], nums[r], target])
                l+=1
                while l < r and nums[l] == nums[l-1]:
                    l +=1
            elif equal > 0:
                r -=1
            elif equal < 0:
                l +=1
        return res
