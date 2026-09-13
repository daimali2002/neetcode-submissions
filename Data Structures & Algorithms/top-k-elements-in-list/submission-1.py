class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lis = {}
        for i in nums:
            if lis.get(i):
                lis[i] += 1
            else:
                lis[i] = 1
        max = 0
        maxnum = -1
        num = []
        while k > 0:
            for i in lis:
                if lis[i] > max:
                    maxnum = i
                    max = lis[i]
            max = 0
            lis[maxnum] = 0
            num.append(maxnum)
            k -= 1
        return num
