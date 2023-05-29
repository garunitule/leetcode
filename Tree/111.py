# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def addDepth(node, depth):
            if node is None:
                return depth

            depth += 1
            # nodeがleafならその時点の深さを返すkaesu
            if node.left is None and node.right is None:
                return depth

            # leftもrightもある場合
            if node.left is not None and node.right is not None:
                return min(addDepth(node.left, depth), addDepth(node.right, depth))
            # leftがない場合（rightはある）
            elif node.left is None:
                return addDepth(node.right, depth)
            # rightがない場合(leftはある)
            else:
                return addDepth(node.left, depth)

        return addDepth(root, 0)