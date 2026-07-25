# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        array = []

        curr = head
        while curr:
            array.append(curr)
            curr = curr.next

        l, r = 0, len(array) - 1
        dummy = ListNode()
        curr = dummy

        while l <= r:
            curr.next = array[l]
            l += 1
            curr = curr.next

            curr.next = array[r]
            r -= 1
            curr = curr.next

        curr.next = None