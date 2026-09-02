class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[1])

        for i in range(len(intervals)-2,-1,-1):
            print(i)
            lastInterval = intervals[i]
            currInterval = intervals[i+1]
            if self.is_overlapping(lastInterval,currInterval):
                intervals.pop(i+1)
                lastInterval[1] = max(lastInterval[1],currInterval[1])
                lastInterval[0] = min(lastInterval[0],currInterval[0])
       
        return intervals

    def is_overlapping(self, interval1, interval2):
        return interval1[1] >= interval2[0]
    