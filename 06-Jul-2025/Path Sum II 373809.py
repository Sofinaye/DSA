# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, current_sum, current_path, result):
            if not node:
                return
            current_path.append(node.val)
            current_sum += node.val
            if not node.left and not node.right:  # Leaf node
                if current_sum == targetSum:
                    result.append(list(current_path))
            else:
                dfs(node.left, current_sum, current_path, result)
                dfs(node.right, current_sum, current_path, result)
            current_path.pop()  # Backtrack
        
        result = []
        dfs(root, 0, [], result)
        return result