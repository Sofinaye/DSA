# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        n = len(piles)
        my_coins = 0
        left = 0
        right = n - 1
        while left < right:
            my_coins += piles[right - 1]
            left += 1
            right -= 2
        return my_coins

        """
        :type piles: List[int]
        :rtype: int
        """
        