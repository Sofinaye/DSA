# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution(object):
    def subarraysDivByK(self, nums, k):
        prefix = 0
        mod_count = defaultdict(int)
        mod_count[0] = 1  
        result = 0
        
        for num in nums:
            prefix = (prefix + num) % k
            if prefix < 0:
                prefix += k
            result += mod_count[prefix]
            mod_count[prefix] += 1
        
        return result
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        