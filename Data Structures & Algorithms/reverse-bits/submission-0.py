class Solution:
    def reverseBits(self, n: int) -> int:
        result: int = 0
        for _ in range(32):
            bit: int = n & 1
            result: int = (result << 1) | bit
            n >>= 1
        return result