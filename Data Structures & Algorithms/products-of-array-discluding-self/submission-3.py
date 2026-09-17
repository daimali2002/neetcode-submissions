class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        count = 0
        zat = -1

        for z, i in enumerate(nums):
            if i == 0:
                count += 1
                zat = z
            else: 
                total *= i
        if count > 1:
            return [0] * len(nums)
        elif count == 1:
            ret = [0] * len(nums)
            ret[zat] = total
            return ret
        else:
            return [total//n for n in nums]