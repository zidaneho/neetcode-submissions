class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rLow = 0
        rHigh = len(matrix) - 1
        cLow = 0
        cHigh = len(matrix[0]) -1

        colLength = len(matrix[0]) - 1

        while rLow <= rHigh and cLow <= cHigh:
            rMid = (rLow + rHigh) // 2
            cMid = (cLow + cHigh) //2
            if target == matrix[rMid][cMid]:
                return True
            if target < matrix[rMid][0]:
                rHigh = rMid - 1
                continue
            elif target > matrix[rMid][colLength]:
                rLow = rMid + 1
                continue
            if target < matrix[rMid][cMid]:
                cHigh = cMid - 1
            elif target > matrix[rMid][cMid]:
                cLow = cMid + 1

        return False
            

        