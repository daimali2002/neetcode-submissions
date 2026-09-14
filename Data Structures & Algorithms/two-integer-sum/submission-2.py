class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mydict = {}
        for i, num in enumerate(nums):
            if target - num  in mydict.keys():
                return [mydict[target - num], i]
            else:
                mydict[num] = i
