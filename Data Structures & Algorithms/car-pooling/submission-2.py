from collections import defaultdict

class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        change = defaultdict(int)

        for num, start, end in trips:
            change[start] += num
            change[end] -= num

        current = 0

        for location in sorted(change):
            current += change[location]

            if current > capacity:
                return False

        return True