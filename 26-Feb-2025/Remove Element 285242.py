# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution(object):
    def removeElement(self, nums, val):
        i = 0 
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        