class Solution:
    def isPalindrome(self, s: str) -> bool:
        fmtStr: str = "".join(c for c in s if c.isalnum()).replace(" ", "").lower()
        return fmtStr == fmtStr[::-1]