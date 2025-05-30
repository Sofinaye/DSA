# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        n = len(temperatures)
        ans = [0] * n 

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return ans
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        