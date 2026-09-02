"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda x: x.start)
        for i in range(len(intervals)-1):
            interval1 = intervals[i]
            interval2 = intervals[i+1]
            if interval1.end > interval2.start:
                return False
        return True