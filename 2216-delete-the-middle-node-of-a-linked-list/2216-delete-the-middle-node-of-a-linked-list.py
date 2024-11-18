# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        prev, slow, fast = head, head, head
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = slow.next
        slow.next = None
        return head