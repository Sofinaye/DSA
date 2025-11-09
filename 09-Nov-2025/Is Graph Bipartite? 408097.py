# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def dfs(self, node, colour, graph, color):
        color[node] = colour  
        for neighbor in graph[node]:
            if color[neighbor] == -1: 
                if not self.dfs(neighbor, 1 - colour, graph, color):
                    return False 
            elif color[neighbor] == colour:
                return False  
        return True  
    def isBipartite(self, graph):
        n = len(graph)
        color = [-1] * n 
        
        for i in range(n):
            if color[i] == -1: 
                if not self.dfs(i, 0, graph, color):
                    return False  
        return True  
        