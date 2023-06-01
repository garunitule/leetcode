# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def calcForEachNode(node):
            node_val = 0
            node_left = None
            node_right = None
            if node is not None:
                node_val += node.val
                node_left = node.left
                node_right = node.right
            return node_val, node_left, node_right

        def mergeNode(node1, node2):
            # どちらもNoneならNoneを返す
            if node1 is None and node2 is None:
                return None

            # どちらかはNoneじゃないので値が決まる
            node_val = 0
            node1_val, node1_left, node1_right = calcForEachNode(node1)
            node_val += node1_val
            node2_val, node2_left, node2_right = calcForEachNode(node2)
            node_val += node2_val
            
            left = mergeNode(node1_left, node2_left)
            right = mergeNode(node1_right, node2_right)
            
            return TreeNode(val=node_val, left=left, right=right)
        
        return mergeNode(root1, root2)
        

# simple answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            root = TreeNode(root1.val + root2.val)
            root.left = self.mergeTree(root1.left, root2.left)
            root.right = self.mergeTree(root2.right, root2.right)
            return root
        # 片方が空の時点で計算する必要はない
        # それ以降の深い階層の計算も不要なので
        else:
            return root1 or root2
        

