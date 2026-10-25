# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        curr = head

        while curr:
            arr.append(curr)
            curr = curr.next

        l, r = 0, len(arr) - 1
        dummy = ListNode()
        curr = dummy

        while l <= r:
            curr.next = arr[l]
            curr = curr.next
            l += 1

            curr.next = arr[r]
            curr = curr.next
            r -= 1

        curr.next = None