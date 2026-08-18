class Solution:
    def numIslands(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0

        rows, cols = len(matrix), len(matrix[0])
        visited = set()
        islands = 0

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or matrix[r][c] == "0" or (r, c) in visited:
                return

            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1

        return islands