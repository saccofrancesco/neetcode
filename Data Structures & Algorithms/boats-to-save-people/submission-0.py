class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        left: int = 0
        right: int = len(people) - 1
        boats: int = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1
        return boats