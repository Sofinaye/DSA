# Problem: Lowest Common Ancestor of Deepest Leaves - https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def findDeepestLeaves(node, depth):
            if not node:
                return (None, depth - 1)
            if not node.left and not node.right:
                return ([node], depth)
            left_leaves, left_depth = findDeepestLeaves(node.left, depth + 1)
            right_leaves, right_depth = findDeepestLeaves(node.right, depth + 1)
            if left_depth > right_depth:
                return (left_leaves, left_depth)
            elif right_depth > left_depth:
                return (right_leaves, right_depth)
            else:
                return (left_leaves + right_leaves, left_depth)
        
        deepest_leaves, max_depth = findDeepestLeaves(root, 0)
        if len(deepest_leaves) == 1:
            return deepest_leaves[0]
        
        def findLCA(node):
            if not node:
                return None
            if node in deepest_leaves:
                return node
            left = findLCA(node.left)
            right = findLCA(node.right)
            if left and right:
                return node
            return left if left else right
        
        return findLCA(root)
