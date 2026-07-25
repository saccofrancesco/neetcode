class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == ".":
                    continue
                bit = 1 << (ord(value) - ord("1"))
                box = (row // 3) * 3 + col // 3
                if rows[row] & bit or cols[col] & bit or boxes[box] & bit:
                    return False
                rows[row] |= bit
                cols[col] |= bit
                boxes[box] |= bit
        return True