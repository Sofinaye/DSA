# Problem: Count Pairs Whose Sum is Less than Target - https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution(object):
    def countPairs(self, nums, target):
        left = 0
        right = len(nums) - 1
        count = 0
        nums.sort()
        print(nums)
        while left < right:
            if nums[left] + nums[right] < target:
                count+= right - left
                left += 1
            else:
                right -= 1
        return count
            

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        