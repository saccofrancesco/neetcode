class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        words = set(wordDict)
        memo = {}

        def dfs(start):
            if start == len(s):
                return [""]

            if start in memo:
                return memo[start]

            result = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word not in words:
                    continue

                sentences = dfs(end)

                for sentence in sentences:
                    if sentence:
                        result.append(word + " " + sentence)
                    else:
                        result.append(word)

            memo[start] = result
            return result

        return dfs(0)