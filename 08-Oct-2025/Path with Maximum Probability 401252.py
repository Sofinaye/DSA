# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))
        
        max_probs = [0.0] * n
        max_probs[start_node] = 1.0
        
        heap = [(-1.0, start_node)]  
        
        while heap:
            neg_prob, node = heapq.heappop(heap)
            curr_prob = -neg_prob
            
            if node == end_node:
                return curr_prob
            
            if curr_prob < max_probs[node]:
                continue
                
            for neighbor, edge_prob in graph[node]:
                new_prob = curr_prob * edge_prob
                
                if new_prob > max_probs[neighbor]:
                    max_probs[neighbor] = new_prob
                    heapq.heappush(heap, (-new_prob, neighbor))
        
        return max_probs[end_node]
