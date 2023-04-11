class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        nr , nc = len(grid)  , len(grid[0])
        
        rooted = []
        
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 2:
                    rooted.append([(r , c)])
                    
                    
                    
        max_minutes = 0
        stack = []
        for r in rooted:
            stack.append(r)
     
        while stack:
            print(stack)
            current = stack.pop() # [(0, 0), (1, 0)]
            max_minutes = max(max_minutes, len(current) - 1)  # First orange was already rotten.
            
            current_orange = current[-1]
           
            row, col = current_orange
            
            targeted_rooted = []
       

            dxn = [
                (1, 0),
                (0, 1),
                (-1, 0),
                (0, -1)
            ]
            for change_x, change_y in dxn:
                currX  = change_x + row
                currY = change_y + col

                if 0 <= currX < nr and 0 <= currY < nc:
                    if grid[currX][currY] == 1:
                        targeted_rooted.append((currX , currY))
                    
        
            
            
            for target in targeted_rooted:  # Append the new orange location, and then rot that orange
                
                row, col = target
                pre_stack = current.copy()
                
                pre_stack.append((row, col))
                stack.insert(0, pre_stack)
                
                
                grid[row][col] = 2  # Rotting!
            
    
    
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    return -1
                
        return max_minutes
            
    