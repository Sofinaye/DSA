# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_map = defaultdict(int)
        n = len(nums1)
        for i in range(n):
            for j in range(n):
                total = nums1[i] + nums2[j]
                sum_map[total] += 1
        
        count = 0
        for k in range(n):
            for l in range(n):
                total = nums3[k] + nums4[l]
                count += sum_map.get(-total, 0)
        
        return count