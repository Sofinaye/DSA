# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution(object):
    def merge(self, intervals):
        intervals.sort(key = lambda i: i[0])
        result = [intervals[0]]
        for start, end in intervals[1:]:
            lastItem = result[-1][1]
            if start <= lastItem:
                result[-1][1] = max(lastItem, end)
            else:
                result.append([start, end])
        return result
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        