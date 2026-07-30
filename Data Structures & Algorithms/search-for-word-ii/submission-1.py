class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.word: str | None = None


class Solution:
    def findWords(
        self,
        board: List[List[str]],
        words: List[str]
    ) -> List[str]:
        root: TrieNode = TrieNode()
        for word in words:
            node: TrieNode = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node: TrieNode = node.children[char]
            node.word = word
        rows: int = len(board)
        cols: int = len(board[0])
        result: List[str] = []
        def dfs(row: int, col: int, parent: TrieNode) -> None:
            char: str = board[row][col]
            if char not in parent.children:
                return
            node: TrieNode = parent.children[char]
            if node.word is not None:
                result.append(node.word)
                node.word = None
            board[row][col] = "#"
            if row > 0 and board[row - 1][col] != "#":
                dfs(row - 1, col, node)
            if row + 1 < rows and board[row + 1][col] != "#":
                dfs(row + 1, col, node)
            if col > 0 and board[row][col - 1] != "#":
                dfs(row, col - 1, node)
            if col + 1 < cols and board[row][col + 1] != "#":
                dfs(row, col + 1, node)
            board[row][col] = char
            if not node.children and node.word is None:
                del parent.children[char]
        for row in range(rows):
            for col in range(cols):
                if board[row][col] in root.children:
                    dfs(row, col, root)
        return result
