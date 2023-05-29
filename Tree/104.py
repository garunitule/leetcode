# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def addDepth(node, depth):
            if node is None:
                return depth
            
            depth += 1
            
            return max(addDepth(node.left, depth), addDepth(node.right, depth))
        
        return addDepth(root, 0)