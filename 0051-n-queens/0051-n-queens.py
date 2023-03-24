class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        main_diag = set()
        post_main_diag = set()
        columns_ = set()
        chess_ = [["."] * n for i in range(n)]
      
        # above all are the case where will be under attack 
        def findWay(each_row):
            if each_row == n:
                string = ["".join(each) for each in chess_]
                result.append(string[:])
                return 
            
            for each_column in range(n):
                if each_column - each_row in main_diag or each_column + each_row in post_main_diag or each_column in columns_:
                    #to avoid attacking of the queens
                    continue
                columns_.add(each_column)
                main_diag.add(each_column - each_row)
                post_main_diag.add(each_column + each_row)
                chess_[each_row][each_column] = "Q"
                #after doing this we have to lookup for any other possiblities 
                findWay(each_row+1)
                #we will be finding any possible way until we are out of rows
                
                
                #Next we will be doing some clean up to restore back to 
                #previous states
                columns_.remove(each_column)
                main_diag.remove(each_column - each_row)
                post_main_diag.remove(each_column + each_row)
                chess_[each_row][each_column] = "."
        findWay(0)
        return result 
                
                