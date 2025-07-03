# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_adj = [[] for _ in range(n)]
        blue_adj = [[] for _ in range(n)]
        
        for u, v in redEdges:
            red_adj[u].append(v)
        for u, v in blueEdges:
            blue_adj[u].append(v)
        
        answer = [-1] * n
        answer[0] = 0  
        
        queue = deque()
        queue.append((0, 0, None))  
        
        visited = [[-1, -1] for _ in range(n)]
        visited[0][0] = 0  
        visited[0][1] = 0 
        
        while queue:
            node, length, last_color = queue.popleft()
            
            if last_color != 0:  
                for neighbor in red_adj[node]:
                    if visited[neighbor][0] == -1:
                        visited[neighbor][0] = length + 1
                        queue.append((neighbor, length + 1, 0))
                        if answer[neighbor] == -1 or length + 1 < answer[neighbor]:
                            answer[neighbor] = length + 1
            
            if last_color != 1:  
                for neighbor in blue_adj[node]:
                    if visited[neighbor][1] == -1:
                        visited[neighbor][1] = length + 1
                        queue.append((neighbor, length + 1, 1))
                        if answer[neighbor] == -1 or length + 1 < answer[neighbor]:
                            answer[neighbor] = length + 1
        
        return answer