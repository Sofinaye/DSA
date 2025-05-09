# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        result = 1
        temp = 2
        count = 0

        while n >= result:
            result += temp
            temp += 1
            count += 1

        return count