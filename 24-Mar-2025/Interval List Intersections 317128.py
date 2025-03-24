# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        i = j = 0
        result = []
        while i < len(firstList) and j < len(secondList):
            first_start, first_end = firstList[i]
            second_start, second_end = secondList[j]
            
            overlap_start = max(first_start, second_start)
            overlap_end = min(first_end, second_end)
            
            if overlap_start <= overlap_end:
                result.append([overlap_start, overlap_end])
            
            if first_end < second_end:
                i += 1
            else:
                j += 1
        return result
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        