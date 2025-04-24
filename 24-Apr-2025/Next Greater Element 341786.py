# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        ans = defaultdict(lambda: -1)
        for num in nums2:
            while stack and stack[-1] < num:
                ans[stack[-1]] = num
                stack.pop()

            stack.append(num)

        return [ans[num] for num in nums1]
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        