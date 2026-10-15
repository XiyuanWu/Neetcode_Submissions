class Solution:
    def exist(self, matrix: List[List[str]], word: str) -> bool:
        if not matrix: return False

        rows, cols = len(matrix), len(matrix[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word): return True

            if r not in range(rows) or c not in range(cols) or (r, c) in visited or matrix[r][c] != word[i]:
                return False

            visited.add((r, c))
            founds = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            visited.remove((r, c))

            return founds

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False