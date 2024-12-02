# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def preorder(node, cur_num):
            nonlocal res
            if not node:
                return
            cur_num = (cur_num * 10) + node.val
            if not (node.left or node.right):
                res += cur_num
            preorder(node.left, cur_num)
            preorder(node.right, cur_num)

        res = 0
        preorder(root, 0)
        return res
