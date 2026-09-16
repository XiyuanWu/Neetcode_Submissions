"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        change = defaultdict(int)

        for interval in intervals:
            change[interval.start] += 1
            change[interval.end] -= 1

        room, result = 0, 0

        for time in sorted(change):
            room += change[time]
            result = max(room, result)

        return result