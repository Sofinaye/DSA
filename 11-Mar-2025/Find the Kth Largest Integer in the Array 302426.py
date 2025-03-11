# Problem: Find the Kth Largest Integer in the Array - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution(object):
    def kthLargestNumber(self, nums, k):
        num = [int(i) for i in nums]
        num.sort()
        result = str(num[-k])
        return result
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        