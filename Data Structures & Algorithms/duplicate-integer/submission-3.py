class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in nums:
            if dict.get(i) == None:
                dict[i] = 1
            else:
                return True
        return False 
         