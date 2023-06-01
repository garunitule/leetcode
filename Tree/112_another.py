# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# スタックを用いて深さ優先探索（DFS）を行った
# この方が最適解にたどり着くまでの時間が短い可能性が高い
# 再帰だと幅優先探索的な近づき方になるし、空間計算量も大きい
# 最悪空間計算量はO(N)(Nはノード数), 直線のような木構造の場合
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        todo = []
        todo.append([root, root.val])
        while len(todo) > 0:
            node, curSum = todo.pop()
            if node.left is None and node.right is None:
                if curSum == targetSum:
                    return True
                continue
            
            if node.left:
                todo.append([node.left, curSum + node.left.val])
            
            if node.right:
                todo.append([node.right, curSum + node.right.val])
        return False