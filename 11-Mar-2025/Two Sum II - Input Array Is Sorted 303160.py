# Problem: Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution(object):
    def twoSum(self, numbers, target):
        hashMap = {}
        for i, num in enumerate(numbers, start = 1):
            if (target - num) in hashMap:
                return [hashMap[target - num], i]
            hashMap[num] = i
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        