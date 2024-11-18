# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy
        while fast:
            to_break = False
            for _ in range(2):
                if fast.next:
                    fast = fast.next
                else:
                    to_break = True
            if to_break:
                break
            slow = slow.next
        if slow.next:
            slow.next = slow.next.next
        return dummy.next
