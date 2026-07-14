# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        arr2 = []

        curr1 = l1
        curr2 = l2

        while curr1:
            arr1.append(str(curr1.val))
            curr1 = curr1.next
        while curr2:
            arr2.append(str(curr2.val))
            curr2 = curr2.next

        num1 = int("".join(arr1[::-1]))
        num2 = int("".join(arr2[::-1]))

        total = str(num1 + num2)[::-1]

        dummy = ListNode()
        curr = dummy

        for d in total:
            curr.next = ListNode(int(d))
            curr = curr.next

        return dummy.next

