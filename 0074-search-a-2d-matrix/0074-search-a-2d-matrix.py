class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows , cols = len(matrix) , len(matrix[0])
        upper = 0
        lower = rows - 1
        #this phase is determing which row the target falls
        while upper <= lower:
            if matrix[upper][-1] < target:
                upper+=1
            elif matrix[lower][0] > target:
                lower-=1
            else:
                break
                
        low , high = 0 , cols-1
        # print(lower)
        while low <= high:
            mid = low + (high-low)//2
            if matrix[lower][mid] == target:
                return True 
            elif matrix[lower][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
        