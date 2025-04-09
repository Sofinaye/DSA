# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution(object):
    def judgeSquareSum(self, c):
        left, right = 0, int(sqrt(c))

        while left <= right:
            total = left**2 + right**2
            if total > c:
                right -=1
            elif total < c:
                left += 1
            else:
                return True
        return False
        """
        :type c: int
        :rtype: bool
        """
        