class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals,key=lambda x: x[1])
        highest = intervals[0][1]
        intervalsRemoved = 0
        for interval in intervals[1:]:
            if interval[0] < highest:
                intervalsRemoved += 1
            else:
                highest = interval[1]
        return intervalsRemoved