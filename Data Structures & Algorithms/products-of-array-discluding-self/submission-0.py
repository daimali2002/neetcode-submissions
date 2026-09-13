class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        for j in range(len(nums)):
            num = 1
            for i in range(len(nums)):
                if i != j:
                    num *= nums[i]
            arr.append(num)
        return arr
        