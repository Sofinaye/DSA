# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        num_provinces = 0

        def dfs(city):
            visited[city] = True
            for neigbhor in range(n):
                if isConnected[city][neigbhor] == 1 and not visited[neigbhor]:
                    dfs(neigbhor)

        for city in range(n):
            if not visited[city]:
                dfs(city)
                num_provinces += 1

        return num_provinces