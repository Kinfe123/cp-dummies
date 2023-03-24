class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nr = len(board)
        nc = len(board[0])
        visited = set()
        def dfs(row  , column , index):
            if index == len(word):
                return True
            if row <  0 or column < 0 or row >= nr or column >= nc or (row , column ) in visited or  word[index] != board[row][column]:
                return False
            
            visited.add((row , column))
            checks = ( dfs(row + 1 , column , index+1)
                or dfs(row-1 , column, index+1)
                or dfs(row  , column+1 , index+1)
                or dfs(row , column-1 , index+1)  )
            visited.remove((row  , column ))
            return checks
        for each_row in range(len(board)):
            for each_column in range(len(board[0])):
                if board[each_row][each_column] == word[0] and dfs(each_row , each_column , 0):
                    return True 
        return False
                
            
        