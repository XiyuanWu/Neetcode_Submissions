class Solution:
    def islandPerimeter(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        perimeter = 0

        

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:

                    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                    for dr, dc in dir:
                        nr, nc = r + dr, c + dc

                        if nr not in range(rows) or nc not in range(cols) or matrix[nr][nc] == 0:
                            perimeter += 1

        return perimeter 