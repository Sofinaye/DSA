# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        return gcd(min_num, max_num)