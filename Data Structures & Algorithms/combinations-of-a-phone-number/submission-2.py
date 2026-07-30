class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping: Dict[str, str] = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result: List[str] = []
        combination: List[str] = []
        def backtrack(index: int) -> None:
            if index == len(digits):
                result.append("".join(combination))
                return
            for letter in mapping[digits[index]]:
                combination.append(letter)
                backtrack(index + 1)
                combination.pop()
        backtrack(0)
        return result