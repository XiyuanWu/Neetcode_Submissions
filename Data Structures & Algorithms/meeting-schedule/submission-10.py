"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: return True
        intervals = [[interval.start, interval.end] for interval in intervals]
        intervals.sort()

        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start < prev_end:
                return False
            prev_end = end
        return True
