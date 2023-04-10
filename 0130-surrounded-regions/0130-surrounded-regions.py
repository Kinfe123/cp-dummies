class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nr , nc = len(board) , len(board[0])
        def explore(r , c):
            if r < 0 or c < 0 or r >= nr or c >= nc or board[r][c] != "O":
                return 
        
            board[r][c] = "p"
            explore(r + 1 , c)
            explore(r - 1,  c )
            explore(r  , c + 1)
            explore(r  , c - 1)
            
        
        for row in range(nr):
            for col in range(nc):
                if board[row][col] == "O" and (row == 0 or row == nr-1) or (col == 0 or col == nc-1):
                    explore(row, col)

        for row in range(nr):
            for col in range(nc):
                if board[row][col] == "O":
                    board[row][col] = "X"
                    
        for row in range(nr):
            for col in range(nc):
                if board[row][col] == "p":
                    board[row][col] = "O"
                    
        
                    