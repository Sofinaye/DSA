# Problem: K Radius Subarray Averages - https://leetcode.com/problems/k-radius-subarray-averages/description/

class Solution(object):
    def getAverages(self, nums, k):
        n = len(nums)
        result = [-1 for i in range(n)]
        pointer = k  

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        

        print(prefix_sum)
        while pointer < n - k:
            avr = (prefix_sum[pointer + k + 1] - prefix_sum[pointer - k]) // (2*k + 1)
            result[pointer] = avr
            pointer += 1

        return result

        
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        