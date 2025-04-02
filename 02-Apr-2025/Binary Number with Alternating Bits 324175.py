# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution(object):
    def hasAlternatingBits(self, n):
        temp = n ^ (n >> 1)
        return (temp & (temp + 1)) == 0
        """
        :type n: int
        :rtype: bool
        """
        