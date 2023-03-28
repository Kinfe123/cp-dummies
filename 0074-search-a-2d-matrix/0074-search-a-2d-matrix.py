class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows , cols = len(matrix) , len(matrix[0])
        upper = 0
        lower = rows - 1
        #this phase is determing which row the target falls
        while upper <= lower:
            mid = upper+(lower-upper)//2
            if matrix[mid][-1] < target:
                upper = mid + 1
            elif matrix[mid][0] > target:
                lower = mid - 1
                #holding the right value
            else:
                break
                
        if not (upper <= lower):
            return False
                
        low , high = 0 , cols-1
        # print(lower)
        lower = upper + (lower-upper)//2
        
        while low <= high:
            mid = low + (high-low)//2
            if matrix[lower][mid] == target:
                return True 
            elif matrix[lower][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
        