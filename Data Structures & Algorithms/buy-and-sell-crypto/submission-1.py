class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # initialize min_price
        min_price = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            profit = abs(prices[i] - min_price)
            if max_profit < profit:
                max_profit = profit
        
        return max_profit