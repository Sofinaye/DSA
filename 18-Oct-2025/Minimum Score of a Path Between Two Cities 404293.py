# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, dist in roads:
            graph[a].append((b, dist))
            graph[b].append((a, dist))
        
        visited = set()
        queue = deque([1])
        visited.add(1)
        
        while queue:
            node = queue.popleft()
            for nei, _ in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)
        
        min_edge = float('inf')
        for a, b, dist in roads:
            if a in visited or b in visited:
                min_edge = min(min_edge, dist)
        
        return min_edge