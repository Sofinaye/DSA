# Problem: Count the Number of Good Subarrays - https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution(object):
    def countGood(self, nums, k):
        count = 0
        left = 0
        freq = defaultdict(int)
        total_pairs = 0
        n = len(nums)
        
        for right in range(n):
            num = nums[right]
            total_pairs += freq[num]
            freq[num] += 1
            
            while total_pairs >= k:
                count += n - right
                left_num = nums[left]
                total_pairs -= (freq[left_num] - 1)
                freq[left_num] -= 1
                left += 1
        
        return count
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        