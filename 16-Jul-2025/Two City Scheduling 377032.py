# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        result = 0
        costs.sort(key=lambda x: x[0] - x[1])
        result = 0
        n = len(costs) // 2
        for i in range(n):
            result += costs[i][0]  
        for i in range(n, 2*n):
            result += costs[i][1]  
        return result