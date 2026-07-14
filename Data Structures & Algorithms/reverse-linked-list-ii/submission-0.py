# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        left_pre, curr = dummy, head
        for i in range(left - 1):
            left_pre, curr = curr, curr.next

        pre = None
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = pre
            pre, curr = curr, temp

        left_pre.next.next = curr
        left_pre.next = pre

        return dummy.next