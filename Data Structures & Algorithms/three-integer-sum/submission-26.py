class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, j in enumerate(nums[:-2]):
            if i == 0 or j != nums[i-1]:
                l, r = i+1, len(nums) - 1        
                while l < r:
                    equal = nums[l] + nums[r] + j
                    if not equal:
                        res.append([nums[l], nums[r], j])
                        l+=1
                        while l < r and nums[l] == nums[l-1]:
                            l +=1
                    elif equal > 0:
                        r -=1
                    elif equal < 0:
                        l +=1
        return res
    
    
        
