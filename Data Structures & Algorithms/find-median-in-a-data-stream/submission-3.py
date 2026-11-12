import heapq

class MedianFinder:

    def __init__(self):
        self.lowerHeap = []
        self.upperHeap = [] 

    def addNum(self, num: int) -> None:
        if len(self.lowerHeap) <= 0 and len(self.upperHeap) >= 0:
            heapq.heappush_max(self.lowerHeap,num)
            return
        
        
        if len(self.lowerHeap) > 0 and num <= self.lowerHeap[0]:
            heapq.heappush_max(self.lowerHeap,num)
        elif len(self.upperHeap) > 0 and num >= self.upperHeap[0]:
            heapq.heappush(self.upperHeap,num)
        else:
            heapq.heappush_max(self.lowerHeap,num)
        
        if abs(len(self.lowerHeap) - len(self.upperHeap)) > 1:
            if len(self.lowerHeap) > len(self.upperHeap):
                l = heapq.heappop_max(self.lowerHeap)
                heapq.heappush(self.upperHeap, l)
            else:
                u = heapq.heappop(self.upperHeap)
                heapq.heappush_max(self.lowerHeap, u)

    def findMedian(self) -> float:
        if (len(self.lowerHeap) + len(self.upperHeap)) % 2 == 0:
            
            return (self.lowerHeap[0] + self.upperHeap[0]) / 2
        else:
            if len(self.lowerHeap) > len(self.upperHeap):
                return self.lowerHeap[0]
            else:
                return self.upperHeap[0]
        