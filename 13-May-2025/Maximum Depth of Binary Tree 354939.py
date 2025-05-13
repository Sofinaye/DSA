# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        countL, countR = 0, 0
        def maxDepth(node):
            if not node:
                return 0

            left = maxDepth(node.left)
            right = maxDepth(node.right)

            return max(left, right) + 1

        
        
        return maxDepth(root)
