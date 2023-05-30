class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _  in range(m)]
        if m == 1 and n == 1:
            return 1
        
        def move(row , col):
            if row >= m or col >= n:
                return 0
            if row == m-1 and col == n-1:
        
                return 1
            if grid[row][col]:
                return grid[row][col]
            grid[row][col] = move(row , col+1) + move(row+1 , col)
            return grid[row][col]
            
            
            
        move(0 , 0)
        print(grid)
    
        return grid[0][0]
                

    