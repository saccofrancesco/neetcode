class TimeMap:

    def __init__(self):
        self.store: dict[int, dict[str, str]] = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[timestamp][key] = value

    def get(self, key: str, timestamp: int) -> str:
        return self.store[timestamp][key]
