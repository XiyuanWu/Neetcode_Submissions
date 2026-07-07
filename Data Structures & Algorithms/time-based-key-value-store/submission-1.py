class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        array = self.store[key]
        result = ""

        l, r = 0, len(array) - 1

        while l <= r:
            mid = (l + r) // 2

            if array[mid][0] <= timestamp:
                result = array[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return result



