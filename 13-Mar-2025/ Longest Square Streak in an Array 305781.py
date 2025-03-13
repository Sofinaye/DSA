# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution(object):
    def longestSquareStreak(self, nums):
        nums.sort()
        num_set = set(nums)
        max_streak = 0
        
        for num in nums:
            current_streak = 1
            current = num
            while current * current in num_set:
                current = current * current
                current_streak += 1
            if current_streak >= 2:
                max_streak = max(max_streak, current_streak)
        return max_streak if max_streak >= 2 else -1
        """
        :type nums: List[int]
        :rtype: int
        """
        