class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash_table: dict[str, int] = {}
        t_hash_table: dict[str, int] = {}
        for char in s:
            if char in s_hash_table:
                s_hash_table[char] += 1
            else:
                s_hash_table[char] = 1
        for char in t:
            if char in t_hash_table:
                t_hash_table[char] += 1
            else:
                t_hash_table[char] = 1
        return s_hash_table == t_hash_table