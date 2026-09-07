from typing import List


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True

        # If there is more than one element, a 1 can never
        # connect to anything because gcd(1, x) = 1.
        if 1 in nums:
            return False

        class DSU:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, a, b):
                root_a = self.find(a)
                root_b = self.find(b)

                if root_a == root_b:
                    return

                if self.rank[root_a] < self.rank[root_b]:
                    root_a, root_b = root_b, root_a

                self.parent[root_b] = root_a

                if self.rank[root_a] == self.rank[root_b]:
                    self.rank[root_a] += 1

        dsu = DSU(n)

        # prime factor -> first index containing that factor
        factor_owner = {}

        for i, value in enumerate(nums):
            x = value
            factor = 2

            while factor * factor <= x:
                if x % factor == 0:
                    # factor is a prime factor of nums[i]
                    if factor in factor_owner:
                        dsu.union(i, factor_owner[factor])
                    else:
                        factor_owner[factor] = i

                    # Remove every occurrence of this prime factor
                    while x % factor == 0:
                        x //= factor

                factor += 1

            # If x > 1, x itself is a remaining prime factor
            if x > 1:
                if x in factor_owner:
                    dsu.union(i, factor_owner[x])
                else:
                    factor_owner[x] = i

        root = dsu.find(0)

        for i in range(1, n):
            if dsu.find(i) != root:
                return False

        return True