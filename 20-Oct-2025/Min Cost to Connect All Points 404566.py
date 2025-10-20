# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        
        visited = [False] * n
        heap = []  
        total_cost = 0
        
        heapq.heappush(heap, (0, 0))
        
        while heap:
            cost, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            total_cost += cost
            
            for v in range(n):
                if not visited[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(heap, (dist, v))
        
        return total_cost