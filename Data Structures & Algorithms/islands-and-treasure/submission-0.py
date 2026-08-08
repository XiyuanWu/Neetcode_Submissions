class Solution:
    def islandsAndTreasure(self, matrix: List[List[int]]) -> None:
        if not matrix: return

        rows, cols = len(matrix), len(matrix[0])
        q = deque()
        inf = 2147483647

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == -1: 
                    continue
                if matrix[r][c] == 0:
                    q.append((r, c))

        while q:
            row, col = q.popleft()
            dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in dir:
                nr, nc = row + dr, col + dc
                if nr in range(rows) and nc in range(cols) and matrix[nr][nc] == inf:
                    matrix[nr][nc] = matrix[row][col] + 1
                    q.append((nr, nc))
                    
                        