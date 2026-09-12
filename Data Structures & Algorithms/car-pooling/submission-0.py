class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        current = 0
        max_end = max(end for i, j, end in trips)  # find max end time

        for i in range(max_end + 1):
            for num, start, end in trips:

                # check someone get off
                if end == i:
                    current -= num

                # check someone get in
                if start == i:
                    current += num

            if current > capacity:
                return False

        return True

        

