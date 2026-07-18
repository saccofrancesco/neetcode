class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs:
            return "-".join(strs)
        return []

    def decode(self, s: str) -> List[str]:
        if s:
            return s.split("-")
        return s