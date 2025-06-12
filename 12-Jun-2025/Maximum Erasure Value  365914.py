# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_sum = 0
        current_sum = 0
        left = 0
        window = set()
        
        for right in range(len(nums)):
            while nums[right] in window:
                window.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            window.add(nums[right])
            current_sum += nums[right]
            max_sum = max(max_sum, current_sum)
        
        return max_sum