class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        change = [0] * 1001

        for num, start, end in trips:
            change[start] += num
            change[end] -= num

        current = 0
        for i in range(1001):
            current += change[i]

            if current > capacity:
                return False

        return True