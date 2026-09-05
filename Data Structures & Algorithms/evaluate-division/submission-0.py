from collections import defaultdict

class Solution:
    def calcEquation(
        self,
        equations: list[list[str]],
        values: list[float],
        queries: list[list[str]]
    ) -> list[float]:

        graph = defaultdict(list)

        # Build weighted graph
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def dfs(start, target, visited):
            if start == target:
                return 1.0

            visited.add(start)

            for neighbor, weight in graph[start]:
                if neighbor not in visited:
                    result = dfs(neighbor, target, visited)

                    if result != -1.0:
                        return weight * result

            return -1.0

        answers = []

        for a, b in queries:
            if a not in graph or b not in graph:
                answers.append(-1.0)
            else:
                answers.append(dfs(a, b, set()))

        return answers