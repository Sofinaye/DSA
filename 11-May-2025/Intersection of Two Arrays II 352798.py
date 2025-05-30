# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        intersection = []
        for num in count1:
            if num in count2:
                intersection.extend([num] * min(count1[num], count2[num]))
        
        return intersection