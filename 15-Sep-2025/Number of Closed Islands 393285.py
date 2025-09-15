# Problem: Number of Closed Islands - https://leetcode.com/problems/number-of-closed-islands/

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 1:
                return
            grid[i][j] = 1
            for dx, dy in directions:
                dfs(i+dx, j+dy)
        
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows-1 or j == 0 or j == cols-1) and grid[i][j] == 0:
                    dfs(i, j)
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    dfs(i, j)
                    count += 1
        return count