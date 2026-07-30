class PrefixTree:

    def __init__(self):
        self.elements: List[str] = []

    def insert(self, word: str) -> None:
        self.elements.append(word)

    def search(self, word: str) -> bool:
        return word in self.elements

    def startsWith(self, prefix: str) -> bool:
        for word in self.elements:
            if word.startswith(prefix):
                return True
        return False