class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twosum(target, nums):
            s = set(nums)

            for i in nums:
                if -(i+target) in s:
                    return [[target, i, -i-target]]
            return []
            



        
        res = set()
        for i, j in enumerate(nums[:-2]):
            for triplet in twosum(j, nums[i+1:]):
                res.add(tuple(sorted(triplet)))

        return [list(x) for x in res]