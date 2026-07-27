# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def search(node, max_so_far):
            nonlocal count
            if not node:
                return

            if node.val >= max_so_far:
                count += 1

            new_max = max(max_so_far, node.val)
            search(node.left, new_max)
            search(node.right, new_max)

        search(root, float("-inf"))
        return count 