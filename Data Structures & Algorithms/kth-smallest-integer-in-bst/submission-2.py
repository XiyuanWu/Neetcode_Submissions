# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []

        def search(node):
            if not node:
                return 

            search(node.left)
            if len(result) == k: return
            result.append(node.val)
            search(node.right)

        search(root)
        return result[-1]