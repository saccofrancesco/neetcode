class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        bracketsMap: dict[str, str] = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        closeOrder: List[str] = list()
        for char in s:
            if char != closeOrder[0]:
                return False
            if char in ["(", "[", "{"]:
                closeOrder.insert(0, bracketsMap[char])
            else:
                closeOrder.pop(0)
        return True