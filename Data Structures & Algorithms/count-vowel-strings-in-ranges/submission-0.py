class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels: set[str] = set("aeiou")
        prefix: list[int] = [0]
        for word in words:
            is_vowel_string: bool = word[0] in vowels and word[-1] in vowels
            prefix.append(prefix[-1] + is_vowel_string)
        ans: list[int] = []
        for left, right in queries:
            ans.append(prefix[right + 1] - prefix[left])
        return ans