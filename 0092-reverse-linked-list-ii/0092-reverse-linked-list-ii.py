# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
head = 0[1,2,3,4,5], left = 2, right = 4
         p 
           c
             n
[1,2]
'''
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        left_prev, cur = dummy, head
        for _ in range(left - 1):
            left_prev, cur = cur, cur.next

        prev = None
        for i in range(right - left + 1):
            temp_next = cur.next
            cur.next = prev
            prev, cur = cur, temp_next

        left_prev.next.next = cur
        left_prev.next = prev

        return dummy.next
