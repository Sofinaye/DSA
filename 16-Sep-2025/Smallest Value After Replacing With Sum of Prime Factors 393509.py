# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        def prime_factor_sum(x):
            total = 0
            temp = x
            d = 2
            while d * d <= temp:
                while temp % d == 0:
                    total += d
                    temp //= d
                d += 1
            if temp > 1:
                total += temp
            return total
        
        while True:
            s = prime_factor_sum(n)
            if s == n:
                break
            n = s
        return n