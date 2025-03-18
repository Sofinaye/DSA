# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution(object):
    def duplicateZeros(self, arr):

        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 1
            i += 1
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        