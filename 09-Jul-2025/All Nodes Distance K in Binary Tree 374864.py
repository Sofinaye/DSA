# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        
        stack = [root]
        parent[root] = None
        while stack:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        
        queue = deque([target])
        visited = set([target])
        level = 0
        while queue and level < k:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                for neighbor in [node.left, node.right, parent[node]]:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            level += 1
        
        result = [node.val for node in queue]
        return result