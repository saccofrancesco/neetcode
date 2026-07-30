class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node: TrieNode = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node: TrieNode = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(index: int, node: TrieNode) -> bool:
            if index == len(word):
                return node.is_word
            char: str = word[index]
            if char == ".":
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            if char not in node.children:
                return False
            return dfs(index + 1, node.children[char])
        return dfs(0, self.root)
