class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack: List[int] = list()
        for asteroid in asteroids:
            alive: bool = True
            while alive and stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] < abs(asteroid):
                    stack.pop()
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                stack.append(asteroid)
        return stack