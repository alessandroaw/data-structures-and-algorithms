# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        temp1 = list1
        temp2 = list2
        start = ListNode(0, None)
        temp = start

        while temp1 and temp2:
            if temp1.val < temp2.val:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next

        while temp1:
            temp.next = temp1
            temp1 = temp1.next
            temp = temp.next

        while temp2:
            temp.next = temp2
            temp2 = temp2.next
            temp = temp.next

        return start.next
