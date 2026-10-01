class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people: list[tuple[int, str]] = list(zip(heights, names))
        people.sort(reverse=True)
        return [name for height, name in people]