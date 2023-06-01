# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def recur(node, curSum):
            if node.left is None and node.right is None:
                return node.val + curSum == targetSum
            
            curSum += node.val
            result = False
            if node.left is not None:
                result = result or recur(node.left, curSum)
            if node.right is not None:
                result = result or recur(node.right, curSum)
            return result
        
        if root is None:
            return False
        return recur(root, 0)
