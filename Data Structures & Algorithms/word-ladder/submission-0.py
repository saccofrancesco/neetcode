from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words: set[str] = set(wordList)
        if endWord not in words:
            return 0
        queue = deque([(beginWord, 1)])
        words.discard(beginWord)
        while queue:
            word, sequence_length = queue.popleft()
            for index in range(len(word)):
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    if letter == word[index]:
                        continue
                    next_word: int = (
                        word[:index]
                        + letter
                        + word[index + 1:]
                    )
                    if next_word == endWord:
                        return sequence_length + 1
                    if next_word in words:
                        words.remove(next_word)
                        queue.append((next_word, sequence_length + 1))
        return 0
