# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        array = []
        for item in lists:
            while item:
                array.append(item.val)
                item = item.next

        array.sort()

        dummy = ListNode()
        curr = dummy

        for i in array:
            curr.next = ListNode(i)
            curr = curr.next

        return dummy.next
