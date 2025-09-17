# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        factors_above = []
        
        i = 1
        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                if i != n // i:
                    factors_above.append(n // i)
            i += 1
        
        total_factors = factors + factors_above[::-1]
        if k <= len(total_factors):
            return total_factors[k-1]
        else:
            return -1