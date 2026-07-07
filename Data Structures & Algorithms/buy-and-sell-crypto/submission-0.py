class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # two pointers
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                maxProfit = max(maxProfit, diff)
            else:
                l = r
            r += 1
        
        return maxProfit