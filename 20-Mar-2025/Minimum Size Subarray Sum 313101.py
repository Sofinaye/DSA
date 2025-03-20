# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        left = 0
        current_sum = 0
        minumum = float("inf")
        for right in range(n):
            current_sum += nums[right]
            
            while current_sum >= target:
                minumum = min(minumum, right - left + 1)
                current_sum -= nums[left]
                left += 1

        if minumum == float("inf"):
            return 0
        else:
            return minumum

        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        