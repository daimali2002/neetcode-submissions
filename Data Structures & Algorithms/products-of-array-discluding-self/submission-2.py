class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = 0
        prod = 1

        for i in nums:
            if i:
                prod *= i
            else:
                zero += 1
        if zero > 1:
            return [0] * len(nums)
        elif zero == 1:
            lis = [0] * len(nums)
            for i in range(len(nums)):
                if not nums[i]:
                    lis[i] = prod
            return lis
        else:
            for i in range(len(nums)):
                nums[i] = prod//nums[i]
        return nums