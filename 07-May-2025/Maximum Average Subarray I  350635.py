# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        temp = sum(nums[ : k])
        maximum = temp
        for i in range(k, n):
            temp = temp + nums[i] - nums[ i - k ] 
            maximum = max(maximum, temp)

        return maximum / k
        