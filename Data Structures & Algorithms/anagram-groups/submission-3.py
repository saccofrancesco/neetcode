class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            counts: List[int] = [0] * 26
            for char in word:
                counts[ord(char) - 97] += 1
            groups[tuple(counts)].append(word)
        return list(groups.values())