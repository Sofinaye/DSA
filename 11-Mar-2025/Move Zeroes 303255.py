# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution(object):
    def moveZeroes(self, nums):
        holder = 0
        for seeker in range(len(nums)):
            if nums[seeker] != 0:
                nums[holder] = nums[seeker]
                holder += 1
        for i in range(holder, len(nums)):
            nums[i] = 0
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        