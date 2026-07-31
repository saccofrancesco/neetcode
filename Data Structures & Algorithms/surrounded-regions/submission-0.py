from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        queue = deque()
        def mark_safe(row: int, col: int) -> None:
            if 0 <= row < rows and 0 <= col < cols and board[row][col] == "O":
                board[row][col] = "#"
                queue.append((row, col))
        for row in range(rows):
            mark_safe(row, 0)
            mark_safe(row, cols - 1)
        for col in range(cols):
            mark_safe(0, col)
            mark_safe(rows - 1, col)
        directions: List[Tuple[int, int]] = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while queue:
            row, col = queue.popleft()
            for row_change, col_change in directions:
                mark_safe(row + row_change, col + col_change)
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "#":
                    board[row][col] = "O"
