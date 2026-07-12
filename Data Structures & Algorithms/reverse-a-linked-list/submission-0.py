# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, curr = None, head

        while curr:
            temp = curr.next
            curr.next = pre  # reverse
            pre = curr       # update pointer
            curr = temp      # update pointer

        return pre