# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        que = deque()
        res = []
        level = 0
        que.append(root)
        while que:
            res.append([])
            nodes_in_level = len(que)
            for i in range(nodes_in_level):
                cur = que.popleft()
                res[level].append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            level += 1
        return res
