class Solution:
    def isNonCyclical(self, n: int) -> bool:
        seen: set[int] = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            total: int = 0
            while n > 0:
                digit: int = n % 10
                total += digit * digit
                n //= 10
            n = total
        return True