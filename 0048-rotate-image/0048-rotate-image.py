class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        It can be done using basic math concept of vectors rotation 
        check this out for reference - https://limnu.com/sketch-easy-90-degree-rotate-vectors/#:~:text=Normally%20rotating%20vectors%20involves%20matrix,swap%20X%20and%20Y%20values.
        
        
        """
        n = len(matrix)
        lists = [[0] * n for _ in range(n)]
        lists1 = []
        start = 0
        
        cpy = matrix.copy()
        for i in range(n):
            for j in range(n):
                lists1.append(cpy[j][i])
            lists1.reverse()
            matrix[start] = lists1
            start+=1
            lists1 = []
            
        return matrix
                
                
                #matrix[i][j] = matrix[j][n-i-1]
               
                
                
                
                
        print(lists)
                                
                                
                
        