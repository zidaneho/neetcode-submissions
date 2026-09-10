"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import math
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        max_heap = []
        intervals = sorted(intervals, key=lambda x: (x.start))
        for interval in intervals:
            if max_heap and max_heap[0] <= interval.start:
                heapq.heapreplace(max_heap,interval.end)
            else:
                heapq.heappush(max_heap,interval.end)
        return len(max_heap)