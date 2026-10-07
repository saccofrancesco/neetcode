class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1: set[int] = set(nums1)
        set2: set[int] = set(nums2)
        return [list(set1 - set2), list(set2 - set1)]