class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [[] for _ in range(len(nums)+1)]
        numcount = {}
        for i in nums:
            numcount[i] = numcount.get(i, 0) + 1
        
        for i in set(nums):
            counts[numcount[i]].append(i)

        ret = []
        for i in range(len(counts)-1,0,-1):
            ret.extend(counts[i])
        return ret[:k]


        