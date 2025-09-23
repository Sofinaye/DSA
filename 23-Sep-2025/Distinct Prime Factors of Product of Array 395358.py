# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        results =set()
        for num in nums:
            n=num
            d=2
            while d*d<=n:
                if n%d==0:
                    results.add(d)
                    while n%d==0:
                        n//=d
                d+=1
            if n>1:
                results.add(n)
        return len(results)