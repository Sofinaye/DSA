# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        ans = []

        for i in range(len(equations)):
            a, b = equations[i]
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))

        def dfs(start, dest, visited):
            if start == dest:
                return 1.0
            visited.add(start)
            for nei, val in graph[start]:
                if nei not in visited:
                    res = dfs(nei, dest, visited)
                    if res != -1.0:
                        return val * res
            return -1.0

        for x, y in queries:
            if x not in graph or y not in graph:
                ans.append(-1.0)
            else:
                visited = set()
                ans.append(dfs(x, y, visited))

        return ans