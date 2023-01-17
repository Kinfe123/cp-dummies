class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        
        Do not return anything, modify matrix in-place instead.
        """
        map_ = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    map_[(i , j)] = 0
        r_limit = len(matrix)-1
        c_limit = len(matrix[0])-1
        for keys , values in map_.items():
            rows , cols = keys 
            up_ , down_ = rows , rows
            right_ , left_ = cols , cols
            
            for up_ in range(rows , -1 , -1):
                matrix[up_][cols] = 0
                
                
            for down_ in range(rows , r_limit+1):
                matrix[down_][cols] = 0
                
            
                
            for left_ in range(0 , cols):
                matrix[rows][left_] = 0
                
            for right_ in range(cols , c_limit+1):
                matrix[rows][right_] = 0
                
        return matrix
                
        
                 
        