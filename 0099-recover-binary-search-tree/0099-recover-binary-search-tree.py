# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
root = [3,1,4,null,null,2]
inorder = [1,3,2,4]
y, x = 2, 3
'''
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        def inorder(r: TreeNode) -> List[int]:
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        def find_two_swapped(nums: List[int]) -> (int, int):
            n = len(nums)
            x = y = None

            for i in range(n - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]
                    # The first swap occurrence
                    if x is None:
                        x = nums[i]
                    # The second swap occurrence
                    else:
                        break
            return x, y

        def recover(r: TreeNode, count: int) -> None:
            if r:
                if r.val == x or r.val == y:
                    r.val = y if r.val == x else x
                    count -= 1
                    if count == 0:
                        return
                recover(r.left, count)
                recover(r.right, count)

        nums = inorder(root)
        x, y = find_two_swapped(nums)
        recover(root, 2)
