# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution(object):
    def findRightInterval(self, intervals):
        n = len(intervals)
        result = [-1] * n

        starts = [(intervals[i][0], i) for i in range(n)]
        starts.sort() 
        
        for i in range(n):
            end = intervals[i][1]  

            for start, index in starts:
                if start >= end:
                    result[i] = index
                    break
        
        return result
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        