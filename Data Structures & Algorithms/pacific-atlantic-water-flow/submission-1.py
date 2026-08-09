class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return None

        rows, cols = len(matrix), len(matrix[0])
        pac_q = deque()
        atl_q = deque()
        pacific = set()
        atlantic = set()

        # pac
        for r in range(rows):
            pac_q.append((r, 0))
            pacific.add((r, 0))

        for c in range(cols):
            pac_q.append((0, c))
            pacific.add((0, c))

        # atl
        for r in range(rows):
            atl_q.append((r, cols - 1))
            atlantic.add((r, cols - 1))

        for c in range(cols):
            atl_q.append((rows - 1, c))
            atlantic.add((rows - 1, c))

        def bfs(q, visited):
            dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while q:
                row, col = q.popleft()
                for dr, dc in dir:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and (r, c) not in visited and matrix[r][c] >= matrix[row][col]:
                        q.append((r, c))
                        visited.add((r, c))

        bfs(pac_q, pacific)
        bfs(atl_q, atlantic)

        return [list(cell) for cell in pacific & atlantic]