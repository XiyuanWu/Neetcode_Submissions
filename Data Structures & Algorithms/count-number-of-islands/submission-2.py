class Solution:
    def numIslands(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0

        rows, cols = len(matrix), len(matrix[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                row, col = q.popleft()
                for dr, dc in dir:
                    nr, nc = row + dr, col + dc

                    if nr in range(rows) and nc in range(cols) and matrix[nr][nc] == "1" and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))


        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands