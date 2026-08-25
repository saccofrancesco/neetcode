class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        # abs(INT_MIN) would exceed the signed 32-bit range
        if x == INT_MIN:
            return 0

        sign = -1 if x < 0 else 1
        x = abs(x)

        result = 0

        while x > 0:
            digit = x % 10
            x //= 10

            # Check overflow BEFORE result * 10 + digit
            if result > INT_MAX // 10:
                return 0

            if result == INT_MAX // 10 and digit > INT_MAX % 10:
                return 0

            result = result * 10 + digit

        return sign * result