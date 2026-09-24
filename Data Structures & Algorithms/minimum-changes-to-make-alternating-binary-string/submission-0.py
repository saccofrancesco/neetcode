class Solution:
    def minOperations(self, s: str) -> int:
        changes_starting_zero: int = 0
        for i in range(len(s)):
            expected: str = "0" if i % 2 == 0 else "1"
            if s[i] != expected:
                changes_starting_zero += 1
        changes_starting_one: int = len(s) - changes_starting_zero
        return min(changes_starting_zero, changes_starting_one)