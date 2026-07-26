class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        array = self.data[key]
        result = ""

        l, r = 0, len(array) - 1

        while l <= r:
            mid = (l + r) // 2

            if array[mid][0] <= timestamp:
                result = array[mid][1]
                l += 1
            else:
                r -= 1

        return result