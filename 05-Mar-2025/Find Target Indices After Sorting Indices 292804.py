# Problem: Find Target Indices After Sorting Indices - https://leetcode.com/problems/find-target-indices-after-sorting-array/description/

class Solution(object):
    def targetIndices(self, nums, target):
        result = []
        nums.sort()
        for i, num in enumerate(nums):
            if target == num:
                result.append(i)
        return result
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        