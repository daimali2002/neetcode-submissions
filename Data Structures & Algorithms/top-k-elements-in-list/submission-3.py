class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        numcount = {}
        ret = []
        for i in nums:
            numcount[i] = numcount.get(i, 0) + 1
        for i,j in numcount.items():
            heapq.heappush(heap,(-j,i))
        for i in range(k):
            ret.append(heapq.heappop(heap)[1])
        return ret


        