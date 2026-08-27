class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result: List[str] = list()
        maxLength: int = max(len(word1), len(word2))
        for i in range(maxLength):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
        return "".join(result)