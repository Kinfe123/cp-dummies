class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        row , col = len(grid) , len(grid[0])
        result = [[None] * col for _ in range(row)]
        
#         def collect(r ,c , left_turn , right_turn):
#             nonlocal left_
#             nonlocal right_
#             nonlocal result
#             if left_turn and r >= 0 and c >= 0:
#                 left_.add(grid[r][c])
#             else:
#                 return len(left_)
#             if right_ and r < row and c < col:
#                 right_.add(grid[r][c])
#             else:
#                 return len(right_)
            
            
#             #recurrence relation 
            
#             result[r][c] = abs(collect(r-1 , c-1 , True , False ) - collect(r + 1 , c+1 , False , True))
#             print('Result: ' , result)
#             left_ = set()
            # right_ = set()
            
            
            
            
            
        def left_collect(r , c , left_count):
            if r >= 0 and r < row and c >= 0 and c < col:
                left_count.add(grid[r][c])
                left_collect(r-1 , c-1 , left_count)
            return left_count
        def right_collect(r , c , right_count):
            if r >= 0 and r < row and c >= 0 and c < col:
                right_count.add(grid[r][c])
                right_collect(r+1 , c+1 , right_count)
            return right_count
        
            
            
       
        for r in range(row):
            for c in range(col):
                left_count = left_collect(r-1, c-1 , set())
                right_count = right_collect(r + 1 , c+1 , set())
            
                result[r][c] = abs(len(left_count) - len(right_count))
        return result
                
        # return result
        
        