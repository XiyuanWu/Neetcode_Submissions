from bisect import bisect_left

class MedianFinder:

    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        index = bisect_left(self.array, num)
        self.array.insert(index, num)

    def findMedian(self) -> float:
        n = len(self.array)

        if n % 2 == 1:
            return self.array[n // 2]
        else:
            mid = n // 2
            return (self.array[mid - 1] + self.array[mid]) / 2
        