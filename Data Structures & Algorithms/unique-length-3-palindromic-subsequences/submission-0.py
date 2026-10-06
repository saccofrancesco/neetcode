class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans: int = 0
        for c in "abcdefghijklmnopqrstuvwxyz":
            left: str = s.find(c)
            right: str = s.rfind(c)
            if left != -1 and left < right:
                middle_chars = set(s[left + 1:right])
                ans += len(middle_chars)
        return ans