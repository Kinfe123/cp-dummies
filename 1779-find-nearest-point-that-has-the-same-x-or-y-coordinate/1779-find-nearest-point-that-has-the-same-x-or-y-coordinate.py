class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance , index  = float('inf') , -1
        for fi , sec in enumerate(points):
            if x == sec[0] or y == sec[1]:
                distance = abs(sec[0] - x) + abs(sec[1] - y)
                # min_distance = min(min_distance , distance):
                if distance < min_distance:
                    
                    min_distance , index = distance , fi
        return index
                    
        
                    
                
                
                
        
        
                
            
            
        