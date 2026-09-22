class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        needed: set[int] = set(nums1)
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                x = stack.pop()
                if x in needed:
                    next_greater[x] = num
            stack.append(num)
        for i, num in enumerate(nums1):
            nums1[i] = next_greater.get(num, -1)
        return nums1