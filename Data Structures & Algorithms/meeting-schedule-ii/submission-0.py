"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0

        max_end = max(interval.end for interval in intervals)
        change = [0] * (max_end + 1)

        for interval in intervals:
            change[interval.start] += 1
            change[interval.end] -= 1

        room, result = 0,  0

        for i in change:
            room += i
            result = max(result, room)

        return result