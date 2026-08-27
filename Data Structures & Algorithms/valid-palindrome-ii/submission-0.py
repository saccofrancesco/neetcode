class Solution:
    def validPalindrome(self, s: str) -> bool:
        possibleSubStrings: List[str] = list()
        for i in range(len(s)):
            sCopy: List[str] = list(s).copy()
            del sCopy[i]
            possibleSubStrings.append(sCopy)
        return any(s == s[::-1] for s in possibleSubStrings)