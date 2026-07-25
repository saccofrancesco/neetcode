class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublist: list[list[str]] = list()
        for word in strs:
            inserted: bool = False
            if sublist:
                for group in sublist:
                    if self.getWordMapping(group[0]) == self.getWordMapping(word):
                        group.append(word)
                        inserted = True
                        break
                if not inserted:
                    sublist.append([word])
            else:
                sublist.append([word])
        return sublist
    
    def getWordMapping(self, word: str) -> dict[str, int]:
        hashTable: dict[str, int] = dict()
        for char in word:
            if char in hashTable:
                hashTable[char] += 1
            else:
                hashTable[char] = 1
        return hashTable