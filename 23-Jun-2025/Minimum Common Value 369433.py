# Problem: Minimum Common Value - https://leetcode.com/problems/minimum-common-value/

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        result = set(nums1)
        for i in  nums2:
            if i in result:
                return i
        return -1