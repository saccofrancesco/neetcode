class Solution:
    def longestPalindrome(self, s: str) -> str:
        start: int = 0
        max_len: int = 1
        def expand(left: int, right: int):
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                length: int = right - left + 1
                if length > max_len:
                    start = left
                    max_len = length
                left -= 1
                right += 1
        for i in range(len(s)):
            # Odd-length palindrome
            expand(i, i)
            # Even-length palindrome
            expand(i, i + 1)
        return s[start:start + max_len]