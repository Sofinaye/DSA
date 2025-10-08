# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution(object):
    def firstMissingPositive(self, nums):
        hashSet = set(nums)
        for i in range(1, len(nums)+2):
            if i not in hashSet:
                return i
        """
        :type nums: List[int]
        :rtype: int
        """
        