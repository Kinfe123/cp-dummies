class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        triangle = []
        
        for i in range(numRows):
            row = [1] * (i + 1)  # create a new row and initialize all values to 1
            
            # calculate the values in the current row
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
                
            triangle.append(row)  # add the current row to the triangle
        
        return triangle