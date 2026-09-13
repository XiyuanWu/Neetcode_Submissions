from bisect import bisect_left

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = bisect_left(intervals, newInterval)
        intervals.insert(index, newInterval)

        result = []

        for start, end in intervals:
            if not result or start > result[-1][1]:
                result.append([start, end])
            else:
                result[-1][0] = min(result[-1][0], start)
                result[-1][1] = max(result[-1][1], end)

        return result