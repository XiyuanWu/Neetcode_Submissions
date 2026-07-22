# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float("-inf")

        def search(node):
            nonlocal result
            if not node:
                return 0

            left = max(0, search(node.left))
            right = max(0, search(node.right))

            result = max(result, node.val + left + right)

            return node.val + max(left, right)

        search(root)
        return result