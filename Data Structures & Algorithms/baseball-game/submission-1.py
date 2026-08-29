class Solution:
    def isInt(self, text: str) -> bool:
        try:
            n: int = int(text)
            return True
        except ValueError:
            return False
    def calPoints(self, operations: List[str]) -> int:
        record: List[int] = list()
        i: int = -1
        for ops in operations:
            if self.isInt(ops):
                record.append(int(ops))
                i += 1
            elif ops == "+":
                record.append(record[i] + record[i - 1])
                i += 1
            elif ops == "D":
                record.append(record[i] * 2)
                i += 1
            elif ops == "C":
                del record[i]
                i -= 1
        return sum(record)