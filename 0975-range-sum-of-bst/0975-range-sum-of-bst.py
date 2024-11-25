# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        res = 0
        stack = [root]

        while stack:
            node = stack.pop()
            if not node:
                continue
            if low <= node.val <= high:
                res += node.val
            if node.val < low:
                stack.append(node.right)
            elif node.val > high:
                stack.append(node.left)
            else:
                stack.append(node.right)
                stack.append(node.left)

        return res
