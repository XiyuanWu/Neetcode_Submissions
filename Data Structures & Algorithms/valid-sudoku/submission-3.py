class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        col = set()
        box = set()

        for r in range(9):
            for c in range(9):
                nums = board[r][c]

                if nums == ".":
                    continue

                row_key = (r, nums)
                col_key = (c, nums)
                box_key = (r // 3, c // 3, nums)

                if row_key in row or col_key in col or box_key in box:
                    return False

                row.add(row_key)
                col.add(col_key)
                box.add(box_key)

        return True