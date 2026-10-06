import random

class RandomizedSet:

    def __init__(self):
        self.values = []
        self.index = {}

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False

        self.index[val] = len(self.values)
        self.values.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False

        remove_index = self.index[val]
        last_value = self.values[-1]

        # Move the last value into the removed value's position
        self.values[remove_index] = last_value
        self.index[last_value] = remove_index

        # Remove the last element
        self.values.pop()
        del self.index[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)