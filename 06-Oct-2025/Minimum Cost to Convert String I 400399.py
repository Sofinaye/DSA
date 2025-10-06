# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = 10**9
        dist = [[INF] * 26 for _ in range(26)]
        
        for i in range(26):
            dist[i][i] = 0
        
        for o, ch, co in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(ch) - ord('a')
            dist[u][v] = min(dist[u][v], co)
        
       
        for k in range(26):
            for i in range(26):
                if dist[i][k] < INF:
                    for j in range(26):
                        if dist[k][j] < INF:
                            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        total = 0
        for sc, tc in zip(source, target):
            if sc == tc:
                continue
            u = ord(sc) - ord('a')
            v = ord(tc) - ord('a')
            if dist[u][v] == INF:
                return -1
            total += dist[u][v]
        
        return total
