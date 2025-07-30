# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        if not prices:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                current_profit = price - min_price
                if current_profit > max_profit:
                    max_profit = current_profit
        
        return max_profit