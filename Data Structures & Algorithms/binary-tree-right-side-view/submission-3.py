# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def search(node, level):
            nonlocal result
            if not node:
                return

            if level == len(result):
                result.append(node.val)

            search(node.right, level + 1)
            search(node.left, level + 1)

        search(root, 0)
        return result