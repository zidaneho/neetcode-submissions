class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in rows[i]:
                    return False
                if val in cols[j]:
                    return False
                if val in squares[(i//3,j//3)]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                squares[(i//3,j//3)].add(val)
        return True
        