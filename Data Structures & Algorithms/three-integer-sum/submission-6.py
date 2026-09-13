class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twosome(nums, target):
            ret = []
            nums.sort()
            start = 0
            end = len(nums) - 1
            while start < end:
                if nums[start] + nums[end] == target:
                    ret.append([nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                elif nums[start] + nums[end] > target:
                    end = end - 1
                else:
                    start = start + 1 
                    
            return ret
        


        ret = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            pairs = twosome(nums[i+1:], -nums[i])
            for pair in pairs:
                ret.append([nums[i]] + pair)
        return ret


        
        