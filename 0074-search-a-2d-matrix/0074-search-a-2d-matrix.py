class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_ = 0
        low  , high = 0 , len(matrix[0])-1
        
        while row_ <= len(matrix)-1:
            
            if target >= matrix[row_][low] and target <= matrix[row_][high]:
                while low <= high:
                    
                    mid = low + (high-low)//2
                    if matrix[row_][mid] == target:
                        return True
                    elif matrix[row_][mid] < target:
                        low = mid + 1
                    else:
                        high = mid - 1
                    
                    
            else:
                row_+=1
                low = 0 
                high = len(matrix[0])-1
        return False
        
        