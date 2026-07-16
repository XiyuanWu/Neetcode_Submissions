# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []

        for item in lists:
            while item:
                arr.append(item.val)
                item = item.next

        arr.sort()

        dummy = ListNode()
        curr = dummy

        for i in arr:
            curr.next = ListNode(i)
            curr = curr.next

        return dummy.next