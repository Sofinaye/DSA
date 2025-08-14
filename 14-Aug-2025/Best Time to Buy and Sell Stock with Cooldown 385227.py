# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        hold = -prices[0]
        sold = 0
        cooldown = 0
        
        for i in range(1, n):
            prev_hold = hold
            prev_sold = sold
            prev_cooldown = cooldown
            
            hold = max(prev_hold, prev_cooldown - prices[i])
            sold = prev_hold + prices[i]
            cooldown = max(prev_cooldown, prev_sold)
        
        return max(sold, cooldown)