class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

      
        m = len(matrix)
        n = len(matrix[0])
        resultlist = [[0] * m for i in range(n)]
        
        for i in range(m):
            for j in range(n):
                resultlist[j][i] = matrix[i][j]
            

        return resultlist








            # [1 , 2 , 3] ,  matrix[1][1] = matrix[1][1] , m[1][2] = m[2][1]
            # [4 , 5 , 6] ,  m[i][j] = m[j][i]  and 
            # [7 , 8 , 9]
