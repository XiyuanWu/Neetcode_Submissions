class Solution:
    def maxAreaOfIsland(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0

        rows = len(matrix)
        cols = len(matrix[0])

        maxArea = 0
        visited = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            area = 0

            while q:
                row, col = q.popleft()
                dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                visited.add((r, c))
                area += 1

                for dr, dc in dir:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and matrix[r][c] == 1 and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))

            return area


        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, bfs(r, c))

        return maxArea