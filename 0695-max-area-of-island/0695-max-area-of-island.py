class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        count = 0
     
        def explore(grid , r , c):
            # nonlocal size
            rowBounded, colBounded = 0 <= r < len(grid), 0 <= c < len(grid[0])
            if not rowBounded or not colBounded:
                return 0
            if grid[r][c] == 0:
                return 0
            if (r,c) in visited:
                return 0
            visited.add((r , c))
            size = 1
            #since we are not able to reach in either of the base cases so we are good to count the entry as 1
     
            # we will explore in every direction using dfs - unidirectinal and commulate the sum of 1's
            size += explore(grid , r - 1 , c) +  explore(grid , r + 1  , c) + explore(grid , r , c - 1) + explore(grid , r , c + 1)

     

           
            
            
            
            return size  
        max_ = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                val =  explore(grid , i , j)
                max_ = max(max_ , val)
        return max_