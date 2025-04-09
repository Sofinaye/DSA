# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        res = 0
        left, middle = 0, 0
        odd = 0
        for right in range(len(nums)):

            if nums[right] % 2:
                odd += 1

            while odd > k:
                if nums[left] % 2:
                    odd -= 1
                left += 1
                middle = left

            if odd == k:
                while not nums[middle] % 2:
                    middle += 1
                
                res += (middle - left) + 1
        
        return res

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        