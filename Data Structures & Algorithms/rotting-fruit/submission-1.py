class Solution:
    def orangesRotting(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0

        rows, cols = len(matrix), len(matrix[0])
        q = deque()
        time, fresh = 0, 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 2:
                    q.append((r, c))
                elif matrix[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in dir:
                    nr, nc = row + dr, col + dc
                    if nr in range(rows) and nc in range(cols) and matrix[nr][nc] == 1:
                        q.append((nr, nc))
                        fresh -= 1
                        matrix[nr][nc] = 2

            time += 1

        return time if fresh == 0 else -1