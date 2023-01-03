class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        map_ = {}
        for i in range(0 , len(mat)):
            for j in range(0 ,len(mat[0])):
                summed = i+j
                if summed not in map_:
                    map_[summed] = [mat[i][j]]
                else:
                    map_[summed] += [mat[i][j]]
                    
        isDown = False
        
        for keys , values in map_.items():
            if isDown:
                for i in values:
                    result.append(i)
            else:
                values.reverse()
                for i in values:
                    result.append(i)
            isDown = not isDown 
        return result 
            
            
                
        
            
        
        