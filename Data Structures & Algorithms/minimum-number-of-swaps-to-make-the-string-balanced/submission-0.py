class Solution:
    def minSwaps(self, s: str) -> int:
        balance: int = 0
        max_imbalance: int = 0
        for char in s:
            if char == '[':
                balance += 1
            else:
                balance -= 1
            max_imbalance: int = max(max_imbalance, -balance)
        return (max_imbalance + 1) // 2