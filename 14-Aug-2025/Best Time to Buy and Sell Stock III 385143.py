# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        first_buy = -prices[0]
        first_sell = 0
        second_buy = -prices[0]
        second_sell = 0
        
        for price in prices[1:]:
            second_sell = max(second_sell, second_buy + price)
            second_buy = max(second_buy, first_sell - price)
            first_sell = max(first_sell, first_buy + price)
            first_buy = max(first_buy, -price)
        
        return second_sell