# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        # find length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # find node before the one we remove
        step = length - n
        curr = dummy

        for _ in range(step):
            curr = curr.next

        # remove the node: curr is one need remove
        curr.next = curr.next.next

        return dummy.next
            