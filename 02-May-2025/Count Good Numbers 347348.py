# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution(object):
    def countGoodNumbers(self, n):
        MOD = 10 ** 9 + 7
        odd = n // 2
        even = n - odd

        def pow(x, n, MOD):

            if n == 0:
                return 1
            if n % 2 == 0:
                half = pow(x, n // 2, MOD)
                return (half * half) % MOD

            return (x * pow(x,n - 1, MOD)) % MOD

          
        return (pow(5, even, MOD) * pow(4, odd, MOD)) % MOD
        """
        :type n: int
        :rtype: int
        """
        