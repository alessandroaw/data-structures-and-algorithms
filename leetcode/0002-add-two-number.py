# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode()
        temp = start
        carry = 0

        # while both list exist create new node with sum as value
        while l1 and l2:
            two_sum = l1.val + l2.val + carry
            carry = two_sum // 10
            remainder = two_sum % 10
            new_node = ListNode(remainder, None)
            temp.next = new_node
            temp = temp.next

            l1 = l1.next
            l2 = l2.next

        # while there is remaining item in one of the list and carry still exist
        # create new node with element + carry  as value
        rl = l1 if l1 else l2
        while rl and carry > 0:
            two_sum = rl.val + carry
            carry = two_sum // 10
            remainder = two_sum % 10
            new_node = ListNode(remainder, None)
            temp.next = new_node
            temp = temp.next
            rl = rl.next

        # if carry does not exist but list still have element
        if carry == 0:
            temp.next = rl

        # if carry still exist create new elemet at the end of the list
        if carry > 0:
            new_node = ListNode(carry, None)
            temp.next = new_node

        return start.next
