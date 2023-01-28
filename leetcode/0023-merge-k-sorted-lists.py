# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeTwoList(l1, l2):
            if not l1 or not l2:
                return l1 if l1 else l2

            if l1.val < l2.val:
                l1.next = mergeTwoList(l1.next, l2)
                return l1
            else:
                l2.next = mergeTwoList(l1, l2.next)
                return l2

        res = lists.pop()
        while lists:
            curr = lists.pop()
            res = mergeTwoList(res, curr)

        return res
