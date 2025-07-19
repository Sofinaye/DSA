# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])
        count = 1  
        last_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] >= last_end:
                count += 1
                last_end = intervals[i][1]
        
        return len(intervals) - count