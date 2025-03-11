# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        result = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            result = max(result, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result
        """
        :type height: List[int]
        :rtype: int
        """
        