class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row , col = len(maze) , len(maze[0])
        def inbound(x , y):
            return 0<=x<row and 0 <=y<col
        def reach(x , y):
            return x == row-1 or y == col-1 or x == 0 or y == 0
        visited = set()
        
        visited.add((entrance[0] , entrance[1]))
        q = deque([(entrance[0] , entrance[1])])
        
        distance = 0
        dxn = [(1 , 0) , (0 , 1) , (-1 , 0) , (0 ,-1)]
        while q:
            
            for i in range(len(q)):
                curr = q.popleft()
                
                if reach(curr[0] , curr[1]):
                    if distance != 0:
                        
                        return distance 
                for dx  , dy in dxn:
                    x = curr[0] + dx
                    y = curr[1] + dy
                    if inbound(x , y) and maze[x][y] == '.' and (x , y) not in visited:
                        q.append((x , y))
                        visited.add((x , y))
            distance += 1
        return -1 

        
        