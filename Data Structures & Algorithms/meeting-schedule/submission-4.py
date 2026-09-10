"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals,key=lambda x: (x.start,x.end))
        for i,interval in enumerate(intervals[:-1]):
            interval2 = intervals[i+1]
            print(interval.start,interval2.start)
            if interval2.start < interval.end:
                return False
        return True
