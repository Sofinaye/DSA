# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            count = 0
            for num in nums:
                
                if (num >> i) & 1:
                    count += 1
            if count % 3 == 1:
                result |= (1 << i)
        if result >= 2**31:
            result -= 2**32
        return result