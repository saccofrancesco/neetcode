class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        target = total // 4

        matchsticks.sort(reverse=True)

        if matchsticks[0] > target:
            return False

        sides = [0, 0, 0, 0]

        def backtrack(i):
            if i == len(matchsticks):
                return True

            stick = matchsticks[i]

            for side in range(4):
                if sides[side] + stick > target:
                    continue

                sides[side] += stick

                if backtrack(i + 1):
                    return True

                sides[side] -= stick

                # If putting the stick on an empty side failed,
                # trying another empty side is equivalent.
                if sides[side] == 0:
                    break

            return False

        return backtrack(0)