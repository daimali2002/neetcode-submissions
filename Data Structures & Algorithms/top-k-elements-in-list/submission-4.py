class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        heap = []
        for i in count.keys():
            heapq.heappush(heap, (-count[i], i))
        ret = []
        for i in range(k):
            ret.append(heapq.heappop(heap)[1])
        return ret