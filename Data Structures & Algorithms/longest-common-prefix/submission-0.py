class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortestWord: str = min(strs, key=len)
        prefix: str = ""
        index: int = 0
        for char in shortestWord:
            if not all(word.startswith(prefix + char) for word in strs):
                break
            prefix += char
        return prefix