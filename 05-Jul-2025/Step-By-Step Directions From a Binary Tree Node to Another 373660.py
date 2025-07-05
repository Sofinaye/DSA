# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find_path(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            if find_path(node.left, target, path):
                path.append('L')
                return True
            if find_path(node.right, target, path):
                path.append('R')
                return True
            return False
        
        start_path = []
        dest_path = []
        
        find_path(root, startValue, start_path)
        find_path(root, destValue, dest_path)
        
        start_path.reverse()
        dest_path.reverse()
        
        i = 0
        while i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]:
            i += 1
        
        path_to_start = start_path[i:]
        path_to_dest = dest_path[i:]
        
        directions = ['U'] * len(path_to_start) + path_to_dest
        
        return ''.join(directions)