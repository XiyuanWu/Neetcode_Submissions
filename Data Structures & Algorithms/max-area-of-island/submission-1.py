class Solution:
    def maxAreaOfIsland(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0

        rows, cols = len(matrix), len(matrix[0])
        visited = set()
        maxA = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            area = 0

            while q:
                row, col = q.popleft()
                dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                area += 1
                for dr, dc in dir:
                    nr, nc = row + dr, col + dc

                    if nr in range(rows) and nc in range(cols) and matrix[nr][nc] == 1 and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))

            return area

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1 and (r, c) not in visited:
                    maxA = max(maxA, bfs(r, c))

        return maxA