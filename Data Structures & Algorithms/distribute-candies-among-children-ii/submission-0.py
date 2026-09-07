import math
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        total = max(math.comb(n+2, 2),0)
        illegal1 = 3*math.comb(max(n - limit + 1,0), 2)
        illegal2 = 3 * math.comb(max(n-2*limit,0),2)
        illegal3 = math.comb(max(n-3*limit-1,0),2)
        return total - illegal1 + illegal2 - illegal3
