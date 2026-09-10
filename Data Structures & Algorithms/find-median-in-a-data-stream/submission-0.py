class MedianFinder:

    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        self.array.append(num)

    def findMedian(self) -> float:
        self.array.sort()

        n = len(self.array)

        if len(self.array) % 2 == 1:
            return self.array[n // 2]
        else:
            mid = n // 2
            return (self.array[mid - 1] + self.array[mid]) / 2

        