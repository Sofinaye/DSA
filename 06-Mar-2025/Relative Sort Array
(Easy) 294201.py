# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        count = Counter(arr1)
        checker = set(arr2)
        result = []
        buffer = []
        for num in arr2:
            for _ in range(count[num]):
                result.append(num)

        for num in arr1:
            if num not in checker:
                buffer.append(num)
        buffer.sort()
        
        return result + buffer
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        