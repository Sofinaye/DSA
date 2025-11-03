# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        max_time = 0
        for i in range(len(processorTime)):
            finish_time = processorTime[i] + tasks[4 * i]
            max_time = max(max_time, finish_time)
        return max_time