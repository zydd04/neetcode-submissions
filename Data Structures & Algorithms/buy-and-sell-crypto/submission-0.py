class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        
        profit  = float('-inf')
        while(l < len(prices) - 1):
            r = len(prices) - 1
            while(l < r):
                if (prices[r] - prices[l] > profit): profit = prices[r] - prices[l]
                r -= 1
            l += 1
        return max(0, profit)
            