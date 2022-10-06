class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        
        i = len(grid) -1 
        j = 0
        count = 0
        x , y = 0 , grid[0]
        while i >= x and j < len(y):
            if grid[i][j] < 0:
                count += len(y) - j
                i-=1 # we look for others
            else:
                j+=1
        return count
    
        