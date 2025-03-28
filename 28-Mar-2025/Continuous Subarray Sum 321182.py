# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution(object):
    def checkSubarraySum(self, nums, k):
        prefix = 0
        mod_map = {0: -1}  
        
        for i in range(len(nums)):
            prefix = (prefix + nums[i]) % k
            if prefix in mod_map:
                if i - mod_map[prefix] >= 2:
                    return True
            else:
                mod_map[prefix] = i
        return False
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        