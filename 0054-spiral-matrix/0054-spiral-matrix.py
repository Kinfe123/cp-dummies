class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        top = 0
        bottom = len(matrix)
        right = len(matrix[0])
        left = 0
        result = []

        while top < bottom and left < right:
            #traversing from left to right horizontally 
            for i in  range(left , right):
                result.append(matrix[top][i])
                
            top+=1
            #traversing from top right to bottom right 
            
            for i in range(top, bottom):
                result.append(matrix[i][right-1])
                

            right-=1
            #traversing from the bottom right to bottom left 
            if top < bottom:
                for i in range(right-1 , left-1 , -1):
                    result.append(matrix[bottom-1][i])
                   

                bottom-=1

            if left < right:
                for i in range(bottom-1, top-1 , -1):
                    result.append(matrix[i][left])
                    
                left+=1
        return result



