class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: list[list[int]],
        queries: list[list[int]]
    ) -> list[bool]:

        reachable = [
            [False] * numCourses
            for _ in range(numCourses)
        ]

        # Direct prerequisites
        for a, b in prerequisites:
            reachable[a][b] = True

        # Find indirect prerequisites
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if reachable[i][k] and reachable[k][j]:
                        reachable[i][j] = True

        return [reachable[u][v] for u, v in queries]