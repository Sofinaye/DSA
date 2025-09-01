# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        for num in nums:
            xor_all ^= num
            
        diff = xor_all & -xor_all
        
        group1 = 0
        group2 = 0
        for num in nums:
            if num & diff:
                group1 ^= num
            else:
                group2 ^= num
                
        return [group1, group2]