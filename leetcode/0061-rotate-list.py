# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # rotate to the right k % length of the list => K
        # rotate is shifting K element from the right to the head
        if not head:
            return head
        if k == 0:
            return head

        prev = None
        temp = head
        k_node = None
        i = 0
        while temp:
            prev = temp
            if i == k:
                k_node = head
            elif i > k:
                k_node = k_node.next
            temp = temp.next
            i += 1

        if not k_node:
            k = k % i
            i = 0
            temp = head
            while temp:
                prev = temp
                if i == k:
                    k_node = head
                elif i > k:
                    k_node = k_node.next
                temp = temp.next
                i += 1

        prev.next = head
        head = k_node.next
        k_node.next = None

        return head
