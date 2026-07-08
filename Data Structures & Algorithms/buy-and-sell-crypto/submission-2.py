class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for p in prices:

            if p < min_price:
                min_price = p
            
            #calculate profit
            profit = p - min_price

            if profit > max_profit:
                max_profit = profit
        
        return max_profit