# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution(object):
    def myPow(self, x, n):
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            ans = helper(x, n // 2)
            ans = ans * ans
            return x * ans if n % 2 else ans

        ans = helper(x, abs(n))
        return ans if n >= 0 else 1 / ans
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        