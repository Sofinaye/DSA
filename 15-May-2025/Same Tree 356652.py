# Problem: Same Tree - https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 = []
        stack2 = []

        def traverse(node, stack):
            if not node:
                stack.append(None)
                return

            traverse(node.left, stack)
            traverse(node.right, stack)
            stack.append(node.val)

        traverse(p, stack1)
        traverse(q, stack2)
        
        return stack1 == stack2