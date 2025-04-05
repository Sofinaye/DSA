# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        arr = [1] * len(nums)
        left = 1
        for i in range(len(nums)):
            arr[i] = left
            left *= nums[i]
        right = 1
        for j in range(len(nums) - 1, -1, -1):
            arr[j] *= right
            right *= nums[j]
        return arr
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        