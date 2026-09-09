class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen = set()

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    number = board[r][c]

                    row_check = (r,number)
                    col_check = (number,c)
                    sub_box_check = (r//3,c//3,number)

                    if row_check in seen or col_check in seen or sub_box_check in seen:
                        return False

                    seen.add(row_check)
                    seen.add(col_check)
                    seen.add(sub_box_check)

        return True