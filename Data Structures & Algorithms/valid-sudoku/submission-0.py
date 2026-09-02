class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.sub1(board) and self.sub2(board) and self.sub3(board)
        
    def sub1(self, board : List[List[str]]) -> bool:
        for row in board:
            table = {}
            for c in row:
                if c == ".":
                    continue
                table[c] = table[c] + 1 if c in table else 1
            for key, val in table.items():
                if val > 1:
                    print("case 1")
                    return False
        return True

    def sub2(self, board : List[List[str]]):
        colTable = [] #index 0 to index 8
        for col in range(9):
            table = {}
            for i in range(9):
                c = board[i][col]
                if c == ".":
                    continue
                table[c] = table[c] + 1 if c in table else 1
                if table[c] > 1:
                    print("case 2")
                    return False
        return True
    def sub3(self, board : List[List[str]]):
        table = {}
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == '.':
                    continue
                key = (i // 3, j // 3)
                if key in table:
                    table[key][c] = table[key][c] + 1 if c in table[key] else 1
                    if table[key][c] > 1:
                        print("case 3",key)
                        return False
                else:
                    table[key] ={}
                    table[key][c] = 1
        return True
        
