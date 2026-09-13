class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        maxprofit = 0
        l, r = 0, 1
        
        for i in range(len(prices)-1):
            maxprofit = max(maxprofit, prices[r] - prices[l])
            if prices[r] <= prices[l]:
                l = r
            r += 1
        return maxprofit
