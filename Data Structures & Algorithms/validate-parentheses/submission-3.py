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
            if char in ["(", "[", "{"]:
                closeOrder.insert(0, bracketsMap[char])
            elif char != closeOrder[0]:
                return False
            else:
                closeOrder.pop(0)
        return True