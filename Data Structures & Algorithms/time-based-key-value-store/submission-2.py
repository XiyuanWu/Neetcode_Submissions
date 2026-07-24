class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = {}

        self.data[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        best_time = -1
        result = ""

        for time, value in self.data[key].items():
            if time <= timestamp and time > best_time:
                best_time = time
                result = value

        return result

