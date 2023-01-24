# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        n_head = head
        i = 0
        while n_head and i < n:
            n_head = n_head.next
            i += 1

        if not n_head:
            return head.next

        temp = head
        n_head = n_head.next
        while n_head:
            n_head = n_head.next
            temp = temp.next

        temp.next = temp.next.next

        return head
