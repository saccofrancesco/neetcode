from collections import defaultdict, deque
from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)

        # Every character must appear in the result,
        # even if it has no edges.
        indegree = {
            char: 0
            for word in words
            for char in word
        }

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            min_len = min(len(w1), len(w2))

            # Invalid prefix case:
            # ["abc", "ab"] cannot be lexicographically sorted.
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            # Only the first differing character matters.
            for j in range(min_len):
                if w1[j] != w2[j]:
                    before = w1[j]
                    after = w2[j]

                    if after not in graph[before]:
                        graph[before].add(after)
                        indegree[after] += 1

                    break

        # Start with all letters that have no prerequisites.
        queue = deque(
            char for char in indegree
            if indegree[char] == 0
        )

        order = []

        while queue:
            char = queue.popleft()
            order.append(char)

            for neighbor in graph[char]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # If we couldn't process every character,
        # the graph contains a cycle.
        if len(order) != len(indegree):
            return ""

        return "".join(order)