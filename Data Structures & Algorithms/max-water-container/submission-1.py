class Solution:
    def maxArea(self, heights: List[int]) -> int:
        highestArea = 0
        low = 0 
        high = len(heights) - 1
        while low < high:
            height = min(heights[low],heights[high])
            length = high - low
            area = height * length
            if area > highestArea:
                highestArea = area
            if heights[low] < heights[high]:
                low += 1
            elif heights[high] < heights[low] :
                high -= 1
            else:
                low +=1 
                high -=1
        return highestArea
            
