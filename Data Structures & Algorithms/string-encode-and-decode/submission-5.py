class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs:
            return "-".join(strs)
        return "empty"

    def decode(self, s: str) -> List[str]:
        if s != "empty":
            return s.split("-")
        return []