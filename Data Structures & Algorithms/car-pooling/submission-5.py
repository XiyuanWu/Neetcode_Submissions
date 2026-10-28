class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        change = [0] * 1001

        for num, start, end in trips:
            change[start] += num
            change[end] -= num

        curr = 0
        for i in range(1001):
            curr += change[i]

            if curr > capacity:
                return False

        return True