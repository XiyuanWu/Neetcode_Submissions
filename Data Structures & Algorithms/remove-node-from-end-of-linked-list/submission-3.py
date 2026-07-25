# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        array = []
        curr = head
        while curr:
            array.append(curr.val)
            curr = curr.next

        del array[len(array) - n]

        dummy = ListNode()

        curr = dummy
        for i in array:
            curr.next = ListNode(i)
            curr = curr.next

        return dummy.next