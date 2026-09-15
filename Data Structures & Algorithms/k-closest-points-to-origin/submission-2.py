import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for point in points:
            heapq.heappush(res,(point[0] * point[0] + point[1] * point[1], point[0],point[1]))
        true_res = []
        for i in range(k):
            distance, x, y = heapq.heappop(res)
            true_res.append([x,y])
        return true_res
