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
            curr = curr.next
            l += 1

            curr.next = array[r]
            curr = curr.next
            r -= 1

        curr.next = None
