"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
'''
root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
stack_p = [5, 3]
stack_q = [1, 3]
'''

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        stack_p, stack_q = [p], [q]
        common_parent = None

        while p.parent or q.parent:
            p, q = stack_p[-1], stack_q[-1]
            if p.parent:
                stack_p.append(p.parent)
            if q.parent:
                stack_q.append(q.parent)

        while stack_p and stack_q:
            p, q = stack_p.pop(), stack_q.pop()
            if p == q:
                common_parent = p

        return common_parent
