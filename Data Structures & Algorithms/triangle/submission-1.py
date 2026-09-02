
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        bottom = triangle[-1][:]
        for row in range(len(triangle)-2,-1,-1):
            for i in range(len(triangle[row])):
                bottom[i] = triangle[row][i] + min(bottom[i], bottom[i+1])
        return bottom[0]
                
