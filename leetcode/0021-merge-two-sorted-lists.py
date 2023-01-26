# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, temp1: Optional[ListNode], temp2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode()
        temp = start

        while temp1 and temp2:
            if temp1.val < temp2.val:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next

        if temp1:
            temp.next = temp1

        if temp2:
            temp.next = temp2

        return start.next
