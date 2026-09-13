class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                maxi = max(prices[j]-prices[i], maxi)
        return maxi 
        