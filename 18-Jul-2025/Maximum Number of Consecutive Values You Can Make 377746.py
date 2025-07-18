# Problem: Maximum Number of Consecutive Values You Can Make - https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/description/

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        current_max = 0
        for coin in coins:
            if coin > current_max + 1:
                break
            current_max += coin
        return current_max + 1