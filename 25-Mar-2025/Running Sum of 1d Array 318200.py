# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution(object):
    def runningSum(self, nums):
        temp = 0
        for i in range(len(nums)):
            nums[i] = nums[i] + temp
            temp = nums[i]
        return nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        