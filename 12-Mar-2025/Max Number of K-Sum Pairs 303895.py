# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution(object):
    def maxOperations(self, nums, k):
        freq = {}
        result = 0
        
        for num in nums:
            complement = k - num
            if complement in freq and freq[complement] > 0:
                result += 1
                freq[complement] -= 1 
            else:
                freq[num] = freq.get(num, 0) + 1
        
        return result
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        