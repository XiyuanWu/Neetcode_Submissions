class Solution:
    def orangesRotting(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0

        rows, cols = len(matrix), len(matrix[0])
        q = deque()
        time = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 2:
                    q.append((r, c))
                if matrix[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            for i in range(len(q)):

                row, col = q.popleft()
                dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            
                for dr, dc in dir:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and matrix[r][c] == 1:
                        q.append((r, c))
                        fresh -= 1
                        matrix[r][c] = 2
            time += 1

        return time if fresh == 0 else -1


