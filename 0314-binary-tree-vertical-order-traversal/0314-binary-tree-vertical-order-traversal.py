# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
{
    0: [3,15]
    -1: [9]
    1: [20]
    2: [7]
}
'''
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        cols_items = defaultdict(list)
        queue = deque([(0, root)])
        min_x, max_x = float(inf), float(-inf)
        res = []

        while queue:
            x, node = queue.popleft()
            cols_items[x].append(node.val)

            min_x, max_x = min(min_x, x), max(max_x, x)

            if node.left:
                queue.append((x - 1, node.left))
            if node.right:
                queue.append((x + 1, node.right))

        for x in range(min_x, max_x + 1):
            res.append(cols_items[x])

        return res
