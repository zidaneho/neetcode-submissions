class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rLow = 0
        rHigh = len(matrix) - 1
        cLow = 0
        cHigh = len(matrix[0]) -1

        colLength = len(matrix[0]) - 1

        rMid = (rLow + rHigh) //2
        while rLow <= rHigh:
            colStart = matrix[rMid][0]
            colEnd = matrix[rMid][colLength]
            if target >= colStart and target <= colEnd:
                break
            if target < colStart:
                rHigh = rMid - 1
            elif target > colEnd:
                rLow = rMid + 1
            rMid = (rLow + rHigh) // 2
        print(rMid)
        while cLow <= cHigh:
            cMid = (cLow + cHigh) // 2
            middle = matrix[rMid][cMid]
            if target == middle:
                return True
            if target < middle:
                cHigh = cMid - 1
            elif target > middle:
                cLow = cMid + 1

        return False
            

        