"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def dfs(n, r, c):
            first = grid[r][c]
            
            for i in range(r, r + n):
                for j in range(c, c + n):
                    if grid[i][j] != first:
                        n = n // 2
                        return Node(
                            True, 
                            False,
                            dfs(n, r, c),
                            dfs(n, r, c + n),
                            dfs(n, r + n, c),
                            dfs(n, r + n, c + n)
                        )

            return Node(first == 1, True)
        return dfs(len(grid), 0, 0) 