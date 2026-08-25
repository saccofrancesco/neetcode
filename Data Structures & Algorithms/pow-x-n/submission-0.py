class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x: float = 1 / x
            n = -n
        result: int = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        return result