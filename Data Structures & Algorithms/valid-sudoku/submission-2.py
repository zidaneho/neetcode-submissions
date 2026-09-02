class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.isValidSudokuBoard(board):
            return False
        if not self.isValidSudokuBoard(self.getBoardGrid(board,0,3,0,3),True):
            return False
        if not self.isValidSudokuBoard(self.getBoardGrid(board,3,6,0,3),True):
            return False
        if not self.isValidSudokuBoard(self.getBoardGrid(board,6,9,0,3),True):
            return False
        if not self.isValidSudokuBoard(self.getBoardGrid(board,0,3,3,6),True):
            return False
        if not self.isValidSudokuBoard(self.getBoardGrid(board,3,6,3,6),True):
            return False
        if not self.isValidSudokuBoard(self.getBoardGrid(board,6,9,3,6),True):
            return False
        if not self.isValidSudokuBoard(self.getBoardGrid(board,0,3,6,9),True):
            return False
        if not self.isValidSudokuBoard(self.getBoardGrid(board,3,6,6,9),True):
            return False
        if not self.isValidSudokuBoard(self.getBoardGrid(board,6,9,6,9),True):
            return False
        
        return True
    def getBoardGrid(self, board, startRow, endRow, startCol, endCol):
        newBoard = []
        localRow = 0
        for i in range(startRow,endRow):
            newBoard.append([])
            for j in range(startCol,endCol):
                newBoard[localRow].append(board[i][j])
            localRow += 1
        return newBoard
    def isValidSudokuBoard(self,board, is_mini = False):
        setRows = [set() for _ in range(len(board))]
        setCols = [set() for _ in range(len(board))]
        total = set()

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] in setRows[i] or board[i][j] in setCols[j]:
                    return False
  
                if is_mini and board[i][j] in total:
                    return False
                if is_mini:
                    total.add(board[i][j])
                setRows[i].add(board[i][j])
                setCols[j].add(board[i][j])
        return True
                