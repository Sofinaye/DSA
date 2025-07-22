# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = [False] * n
        visited = [0] * n  

        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True
            visited[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visited[node] = 2
            return True

        result = []
        for i in range(n):
            if dfs(i):
                result.append(i)
        return result