class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twosum(target, nums):
            s = set(nums)

            for i in nums:
                if -(i+target) in s:
                    return [[target, i, -i-target]]
            return []
            



        nums = list(set(nums))
        res = []
        for i, j in enumerate(nums[:-2]):
            res.extend(twosum(j, nums[i+1:]))
        return res