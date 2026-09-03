from collections import defaultdict, OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # key -> [value, frequency]
        self.cache = {}

        # frequency -> OrderedDict of keys
        self.freq = defaultdict(OrderedDict)

        # Smallest frequency currently present
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        value, frequency = self.cache[key]

        # Remove key from its current frequency bucket
        del self.freq[frequency][key]

        # If this bucket became empty, clean it up
        if not self.freq[frequency]:
            del self.freq[frequency]

            if self.min_freq == frequency:
                self.min_freq += 1

        # Increase frequency
        frequency += 1
        self.cache[key] = [value, frequency]

        # Add key as the most recently used
        # inside the new frequency bucket
        self.freq[frequency][key] = None

        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        # Key already exists:
        # updating it also counts as a use
        if key in self.cache:
            self.cache[key][0] = value
            self.get(key)
            return

        # Cache full: evict LFU, and if tied, LRU
        if len(self.cache) == self.capacity:
            key_to_remove, _ = self.freq[self.min_freq].popitem(last=False)

            del self.cache[key_to_remove]

            if not self.freq[self.min_freq]:
                del self.freq[self.min_freq]

        # New keys always start at frequency 1
        self.cache[key] = [value, 1]
        self.freq[1][key] = None
        self.min_freq = 1