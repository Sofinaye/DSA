# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mySet = set(nums)
        for i in range(len(nums) + 1):
            if i not in mySet:
                return i
        