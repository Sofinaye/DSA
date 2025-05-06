# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        l, r = 1, n
        while l < r:
            if isBadVersion((l + r) // 2):
                r = (l + r)// 2
            else:
                l = (l + r) // 2 + 1
        return l
        """
        :type n: int
        :rtype: int
        """
        