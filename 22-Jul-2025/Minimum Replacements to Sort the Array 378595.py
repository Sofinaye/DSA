# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        operations = 0
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                splits = math.ceil(nums[i] / nums[i + 1])
                operations += splits - 1
                nums[i] = nums[i] // splits
        return operations