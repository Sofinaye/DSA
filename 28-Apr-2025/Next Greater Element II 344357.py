# Problem: Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/

class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []
        
        for i in range(2 * n):
            index = i % n
            while stack and nums[stack[-1]] < nums[index]:
                res[stack.pop()] = nums[index]
            if i < n:
                stack.append(index)
        
        return res
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        