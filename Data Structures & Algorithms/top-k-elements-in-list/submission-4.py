class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        buckets = [None] * (len(nums) + 1)
        for num, count in frequency.items():
            bucket = buckets[count]
            if bucket is None:
                buckets[count] = [num]
            else:
                bucket.append(num)
        result = []
        for count in range(len(buckets) - 1, 0, -1):
            bucket = buckets[count]
            if bucket is not None:
                result.extend(bucket)
                if len(result) >= k:
                    return result[:k]