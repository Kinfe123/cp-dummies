class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        directions = {
            1:[(0, -1) , (0, 1)],
            2:[(1 , 0) , (-1 , 0)],
            3:[(0 , -1) , (1 ,0)],
            4:[(0  , 1) , (1 , 0)],
            5:[(0 , -1) , (-1 , 0)],
            6:[(0 , 1) , (-1 ,0)]
            
        }
        
        def isbound(row , col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        visited = set()
        q  = deque()
        visited.add((0 , 0))
        
        source = (0 , 0)
        def dfs(row , col):
            visited.add((row , col))
            if row == len(grid)-1 and col == len(grid[0])-1:
                return True 
            pos_element = grid[row][col]
            
            for dxn in directions[pos_element]:
                dx , dy = dxn
                new_x , new_y = dx + row,  dy + col
                #to make sure it is connected we have to look back from the current position like we have to take 
                #the negative to make sure it is found on next position that we are travelling 
                connected = isbound(new_x , new_y) and (-dx , -dy) in directions[grid[new_x][new_y]] 
                if isbound(new_x , new_y) and (new_x , new_y) not in visited and connected:
                    visited.add((new_x , new_y))
                    res = dfs(new_x , new_y)
                    if res:
                        return True
            return False
        return dfs(0, 0)
                
        