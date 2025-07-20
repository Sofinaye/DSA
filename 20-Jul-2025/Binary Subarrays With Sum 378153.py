# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        current_sum = 0
        result = 0
        
        for num in nums:
            current_sum += num
            result += prefix_counts.get(current_sum - goal, 0)
            prefix_counts[current_sum] += 1
        
        return result