class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0:
            return False

        target = total // k

        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        buckets = [0] * k

        def backtrack(i):
            if i == len(nums):
                return True

            num = nums[i]
            seen = set()

            for j in range(k):
                # Don't try buckets with the same current sum
                if buckets[j] in seen:
                    continue

                if buckets[j] + num > target:
                    continue

                seen.add(buckets[j])

                buckets[j] += num

                if backtrack(i + 1):
                    return True

                buckets[j] -= num

            return False

        return backtrack(0)