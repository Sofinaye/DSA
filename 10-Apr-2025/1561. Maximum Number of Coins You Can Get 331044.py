# Problem: 1561. Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/

class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        n = len(piles)
        coins = 0
        left = 0
        right = n - 1
        while left < right:
            coins += piles[right - 1]
            left += 1
            right -= 2
        return coins

        """
        :type piles: List[int]
        :rtype: int
        """
        