class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = max_v = 0
    
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            max_v = max(max_v, prices[r] - prices[l])
        return max_v