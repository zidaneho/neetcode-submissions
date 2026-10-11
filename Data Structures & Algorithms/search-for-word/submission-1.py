class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        for i,row in enumerate(board):
            for j,ch in enumerate(row):
                visited = set()
                self.found = False
                def dfs(row,col,index):
                    if (row, col) in visited or (row < 0 or row >= len(board) or col < 0 or col >= len(board[row])):
                        return
                    if board[row][col] != word[index]:
                        return
                    if index == len(word) - 1:
                        self.found=True
                        return
                    
                    visited.add((row,col))
                    dfs(row+1,col,index+1)
                    dfs(row-1,col,index+1)
                    dfs(row,col+1,index+1)
                    dfs(row,col-1,index+1)
                    visited.remove((row,col))
                dfs(i,j,0)
                if self.found:
                    return True
        return False