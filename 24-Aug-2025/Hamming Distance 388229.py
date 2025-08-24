# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = x ^ y
        count = 0
        while result:
            count += result & 1
            result >>= 1
        return count