# Problem: Number of Ways to Arrive at Destination - https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = defaultdict(list)
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))
        
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        
        heap = [(0, 0)] 
        
        while heap:
            time, node = heappop(heap)
            if time > dist[node]:
                continue
            for nei, travel in graph[node]:
                new_time = time + travel
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    ways[nei] = ways[node]
                    heappush(heap, (new_time, nei))
                elif new_time == dist[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % MOD
        
        return ways[n - 1] % MOD