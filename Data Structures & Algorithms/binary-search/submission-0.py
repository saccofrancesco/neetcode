class Solution:
    def search(self, nums: List[int], target: int) -> int:
        copy: List[int] = nums.copy()
        while True:
            if len(copy) == 1 and copy[0] != target:
                return -1
            pivot: int = len(copy) // 2
            if copy[pivot] > target:
                copy = nums[:pivot]
            elif copy[pivot] <  target:
                copy = nums[pivot + 1:]
            else:
                return pivot