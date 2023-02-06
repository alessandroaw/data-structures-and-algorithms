# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1 -> 2 -> 3 -> 4 -> 5
        # 4 -> 5 -> 1 -> 2 -> 3
        # h - k

        if not head or not head.next or not k:
            return head

        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        k = k % n
        if not k:
            return head
        prev = None
        curr = head
        for _ in range(n - k):
            prev = curr
            curr = curr.next

        prev.next = None
        tail.next = head

        return curr
