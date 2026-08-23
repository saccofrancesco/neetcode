class Solution:
    def checkValidString(self, s: str) -> bool:
        minOpen: int = 0
        maxOpen: int = 0
        for char in s:
            if char == "(":
                minOpen += 1
                maxOpen += 1
            elif char == ")":
                minOpen -= 1
                maxOpen -= 1
            else:  # '*'
                minOpen -= 1
                maxOpen += 1
            if maxOpen < 0:
                return False
            minOpen = max(minOpen, 0)
        return minOpen == 0