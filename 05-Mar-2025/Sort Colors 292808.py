# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution(object):
    def sortColors(self, nums):
        low = 0
        high = len(nums) - 1
        current = 0
        
        while current <= high:
            if nums[current] == 0:
                nums[current], nums[low] = nums[low], nums[current]
                current += 1
                low += 1
            elif nums[current] == 2:
                nums[current], nums[high] = nums[high], nums[current]
                high -= 1
            else:
                current += 1
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        