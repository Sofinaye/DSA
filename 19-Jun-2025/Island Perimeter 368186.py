# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            
            if (i, j) in visited:
                return 0

            visited.add((i, j))

            per = dfs(i, j + 1)
            per += dfs(i + 1, j)
            per += dfs(i, j - 1)
            per += dfs(i - 1, j)
            return per

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i, j)