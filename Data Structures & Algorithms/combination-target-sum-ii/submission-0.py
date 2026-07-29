class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result: List[List[int]] = []
        combination: List[int] = []
        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(combination.copy())
                return
            for i in range(start, len(candidates)):
                value: int = candidates[i]
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if value > remaining:
                    break
                combination.append(value)
                backtrack(i + 1, remaining - value)
                combination.pop()
        backtrack(0, target)
        return result