"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':

        def inorder(node):
            nonlocal first, last
            if node:
                inorder(node.left)

                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node
                last = node

                inorder(node.right)

        if not root:
            return root

        first, last = None, None
        inorder(root)

        last.right = first
        first.left = last
        return first