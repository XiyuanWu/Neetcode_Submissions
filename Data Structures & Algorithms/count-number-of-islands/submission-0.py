class Solution:
    def numIslands(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in dir:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and matrix[r][c] == "1" and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))


        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands