# Problem: Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def helper(mid):
            total = 0
            for num in nums:
                total += ceil(num / mid)

                if total > threshold:
                    return False
            return True
        
        l, r = 0, 10**6
        while r - l > 1:
            mid = l + (r - l) // 2

            if helper(mid):
                r = mid
            else:
                l = mid
        return r