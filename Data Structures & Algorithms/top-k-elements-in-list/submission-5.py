class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        bucket = [[] for i in range(len(nums) + 1)]
        for i in nums:
            count[i] += 1
        for i,j in count.items():
            bucket[j].append(i)
        
        ret = []

        for i in range(len(nums), 0, -1):
            ret += bucket[i]
        return ret[0:k]