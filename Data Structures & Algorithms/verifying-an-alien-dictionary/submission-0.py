class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        rank: Dict[str, int] = {char: i for i, char in enumerate(order)}
        for i in range(len(words) - 1):
            word1: str = words[i]
            word2: str = words[i + 1]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if rank[word1[j]] > rank[word2[j]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True