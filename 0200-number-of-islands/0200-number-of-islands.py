class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        def explore(grid , r , c):
            rowBounded, colBounded = 0 <= r < len(grid), 0 <= c < len(grid[0])
            if not rowBounded or not colBounded:
                return False
            if grid[r][c] == "0":
                return False
            if (r,c) in visited:
                return False
            visited.add((r , c))
     
       
            explore(grid , r - 1 , c)

            explore(grid , r + 1  , c)
     
            explore(grid , r , c - 1)
            explore(grid , r , c + 1)

            
            return True 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if explore(grid , i , j):
                    count+=1
        return count
        
        